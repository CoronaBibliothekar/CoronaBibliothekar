
import yaml

with open("responses.yml", 'r') as stream:
    try:
        responses = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

from bs4 import BeautifulSoup
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from Levenshtein import distance


bundeslaender = ["Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Bremen", "Hamburg", "Hessen",
                 "Mecklenburg-Vorpommern", "Niedersachsen", "Nordrhein-Westfalen", "Rheinland-Pfalz",
                 "Saarland", "Sachsen", "Sachsen-Anhalt", "Schleswig-Holstein", "Thüringen"]

# gibt die tabelle des rki zurück, als liste in der alle zeilen aneinandergehängt sind.
def getcurrent_nubers() -> List[str]:
    url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return [x.get_text().replace(".", "") for x in soup.find_all("td", attrs={"class": "center", "colspan": "1", "rowspan": "1"})]

# antwortet auf alle fragen bezüglich der aktuellen Zahlen, welche vom rki abgelesen werden können
class ActionCurrentNumbers(Action):
    def name(self) -> Text:
        return "action_current_numbers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            current_numbers = getcurrent_nubers()

            #slots auslesen und falls nicht vorhanden als leeren sting setzen, damit distanzfunktion klappt.
            location = tracker.get_slot("location")
            if location is None:
                location = ""
            metric = tracker.get_slot("metric")
            if metric is None:
                metric = ""

            # Levenshtein distanz um trotz rechtschreibfehlern noch die richtigen daten zu liefern.
            distance_infected = min([distance(metric, x) for x in ["", "Infiziert", "Infektionen", "Fälle", "Infektionszahlen"]])
            distance_deaths = min([distance(metric, x) for x in ["Tote", "gestorben", "Todesfälle", "Toten"]])

            distance_germany = min([distance(location, x) for x in ["Deutschland", "", "Bundesweit"]])
            distance_corona_bundesland = min([distance(location, x) for x in bundeslaender])

            if (distance_germany < distance_corona_bundesland):
                if distance_infected < distance_deaths:
                    # Infizierte in ganz Deutschland
                    dispatcher.utter_message(
                        text="Laut RKI befindet sich die Anzahl der bestätigten Corona-Virus Infektionen in Deutschland aktuell bei {}  https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html".format(
                            current_numbers[-4]))
                else:
                    # Tote in ganz Deutschland
                    dispatcher.utter_message(
                        text="Laut RKI befindet sich die Anzahl der Todesfälle aufgrund von Corona-Virus in Deutschland aktuell bei {}  https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html".format(
                            current_numbers[-1]))
            else:
                # Levenshtein distanz um trotz rechtschreibfehlern noch die richtigen daten zu liefern.
                distance_bundeslaender = [distance(location, x) for x in bundeslaender]
                bundesland = list(sorted(zip(distance_bundeslaender, bundeslaender)))[0][1]
                if distance_infected < distance_deaths:
                    # Infizierte in einem Bundesland
                    infected_in_bundesland = current_numbers[bundeslaender.index(bundesland)*4]
                    dispatcher.utter_message(
                        text="Laut RKI befindet sich die Anzahl der bestätigten Corona-Virus Infektionen in {} aktuell bei {}  https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html".format(
                            bundesland, infected_in_bundesland))
                else:
                    # Tote in einem Bundesland
                    deaths_in_bundesland = current_numbers[bundeslaender.index(bundesland) * 4 + 2]
                    dispatcher.utter_message(
                        text="Laut RKI befindet sich die Anzahl der Todesfälle aufgrund von Corona-Virus in {} aktuell bei {}  https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html".format(
                            bundesland, deaths_in_bundesland))


        except Exception as e:
            dispatcher.utter_message(text=responses.get("Beim laden der aktuellen Zahlen ist was schiefgelaufen. Schau mal bei https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html vorbei, da sind immer die aktuellen Zahlen zu sehen"))
            print("Aktuelle Fallzahl konnte nicht geladen werden")
            print(e)
        return []


#antwortet auf die Frage welche bundesländer am schlimmsten getroffen wurden
class ActionCurrentBundeslaender(Action):
    def name(self) -> Text:
        return "action_current_bundeslaender"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[
        Dict[Text, Any]]:
        try:
            aktuelle_zahlen = getcurrent_nubers()

            # Gesamtzahl der Infektionen in den einzelnen Bundesländern
            infected = []
            for i in range(len(bundeslaender)):
                infected.append(int(aktuelle_zahlen[4*i].replace(".", "")))

            # Sortiere Bundesländer nach anzahl der Infizierten
            sorted_bundeslaender = list(reversed(sorted(zip(infected, bundeslaender))))

            tracker.get_latest_entity_values()

            dispatcher.utter_message(text="Laut RKI sind sind aktuell {}({} Infektionen), {}({} Infektionen) und {}({} Infektionen) am schlimmsten Betroffen  https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html".format(
                sorted_bundeslaender[0][1],
                sorted_bundeslaender[0][0],
                sorted_bundeslaender[1][1],
                sorted_bundeslaender[1][0],
                sorted_bundeslaender[2][1],
                sorted_bundeslaender[2][0]
            ))

        except Exception as e:
            dispatcher.utter_message(text=responses.get("current_bundeslaender_fallback"))
            print("Aktuelle Fallzahl konnte nicht geladen werden")
            print(e)

        return []