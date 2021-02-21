from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict

# show projects
class ValidateRegisterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_register_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
         return {"registeremail": None}
        else: 
         return {"registeremail": slot_value}	
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_submitregister"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
	
        user_name = tracker.get_slot("registeremail")
        print("email id  is  : ",user_name) 
        
		
        dispatcher.utter_message(template="utter_details_thanks")
        return[]

