
import yaml

with open("responses.yml", 'r') as stream:
    try:
        responses = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

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
