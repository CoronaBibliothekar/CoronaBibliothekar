# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import yaml

with open("responses.yml", 'r') as stream:
    try:
        responses = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

import operator
from bs4 import BeautifulSoup
import requests
from typing import Any, Text, Dict, List
from Levenshtein import distance
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionWhatIs(Action):
    def name(self) -> Text:
        return "action_what_is"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        topic = str(tracker.get_slot('topic'))

        distance_covid = min([distance(topic, x) for x in ["Covid", "Virus", "Covid19", "covid", "covid19"]])
        distance_corona = min([distance(topic, x) for x in ["Corona", "Coronavirus", "Coronaviren"]])

        if (distance_corona < distance_covid):
            dispatcher.utter_message(text=responses.get("what_is_corona"))
        else:
            dispatcher.utter_message(text=responses.get("what_is_covid"))

        return []


class ActionWhatIs(Action):
    def name(self) -> Text:
        return "action_difference"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        topic = str(tracker.get_slot('topic'))

        distance_flu = min([distance(topic, x) for x in ["Grippe", "Influenza"]])
        distance_sars_mers = min([distance(topic, x) for x in ["Sars", "Mers"]])

        if (distance_flu < distance_sars_mers):
            dispatcher.utter_message(text=responses.get("difference_flu"))
        else:
            dispatcher.utter_message(text=responses.get("difference_sars_mers"))

        return []


class ActionCurrentInfected(Action):
    def name(self) -> Text:
        return "action_current_infected"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')

            tds = soup.find_all("td", attrs={"class": "center", "colspan": "1", "rowspan": "1"})
            current_infected = (tds[-4].get_text())
            dispatcher.utter_message(
                text="Laut RKI befindet sich die Anzahl der bestätigten Corona-Virus Infektionen in Deutschland aktuell bei {}".format(
                    current_infected))
        except Exception as e:
            dispatcher.utter_message(text=responses.get("current_infected_fallback"))
            print("Aktuelle Fallzahl konnte nicht geladen werden")
            print(e)
        return []


class ActionCurrentInfected(Action):
    def name(self) -> Text:
        return "action_current_deaths"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')

            tds = soup.find_all("td", attrs={"class": "center", "colspan": "1", "rowspan": "1"})
            current_dead = (tds[-1].get_text())
            dispatcher.utter_message(
                text="Laut RKI befindet sich die Anzahl der Todesfälle aufgrund von Corona-Virus in Deutschland aktuell bei {}".format(
                    current_dead))
        except Exception as e:
            dispatcher.utter_message(text=responses.get("current_dead_fallback"))
            print("Aktuelle Fallzahl konnte nicht geladen werden")
            print(e)
        return []


class ActionCurrentInfected(Action):
    def name(self) -> Text:
        return "action_current_bundeslaender"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[
        Dict[Text, Any]]:
        url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')

            tds = soup.find_all("td", attrs={"class": "center", "colspan": "1", "rowspan": "1"})

            bundeslaender = ["Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Bremen", "Hamburg", "Hessen",
                             "Mecklenburg-Vorpommern", "Niedersachsen", "Nordrhein-Westfalen", "Rheinland-Pfalz",
                             "Saarland", "Sachsen", "Sachsen-Anhalt", "Schleswig-Holstein", "Thüringen"]

            infected = []
            for i in range(len(bundeslaender)):
                infected.append(int(tds[4*i].get_text().replace(".", "")))

            sorted_bundeslaender = list(reversed(sorted(zip(infected, bundeslaender))))

            dispatcher.utter_message(text="Laut RKI sind sind aktuell {}({} Infektionen), {}({} Infektionen) und {}({} Infektionen) am schlimmsten Betroffen".format(
                sorted_bundeslaender[0][0],
                sorted_bundeslaender[0][1],
                sorted_bundeslaender[1][0],
                sorted_bundeslaender[1][1],
                sorted_bundeslaender[2][0],
                sorted_bundeslaender[2][1]
            ))

        except Exception as e:
            dispatcher.utter_message(text=responses.get("current_bundeslaender_fallback"))
            print("Aktuelle Fallzahl konnte nicht geladen werden")
            print(e)

        return []
