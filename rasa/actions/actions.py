# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import speech_recognition as sr
# import pyttsx3
#
#
# class ActionAskPython(Action):
#
#     def name(self) -> Text:
#         return "action_ask_python"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         response_text = "Python is an interpreted, high-level, general-purpose programming language."
#         dispatcher.utter_message(text=response_text)
#
#         # Convert text to speech
#         tts_engine = pyttsx3.init()
#         tts_engine.say(response_text)
#         tts_engine.runAndWait()
#
#         return []
#
#
# class ActionAskFlask(Action):
#
#     def name(self) -> Text:
#         return "action_ask_flask"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         response_text = "Flask is a micro web framework written in Python."
#         dispatcher.utter_message(text=response_text)
#
#         # Convert text to speech
#         tts_engine = pyttsx3.init()
#         tts_engine.say(response_text)
#         tts_engine.runAndWait()
#
#         return []
