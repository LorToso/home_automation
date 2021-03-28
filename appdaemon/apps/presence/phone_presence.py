import appdaemon.plugins.hass.hassapi as hass
from lamp_group import LampGroup

from helpers import safe_get_app
from notifier.actionable_notification import ActionableNotification


class PhonePresence(hass.Hass):

    entity_id: str = ""
    lamp_group: LampGroup

    def initialize(self) -> None:
        self.entity_id = self.args["entity_id"]
        self.lamp_group = safe_get_app(self, self.args["lamp_group"])

        self.listen_state(self.on_state, entity=self.entity_id)
        self.listen_event(self.on_event, event="mobile_app_notification_action")

    def on_state(self, entity, attribute, old, new, kwargs) -> None:

        if old == "home" and new == "not_home":
            self.log("Left home")
            lamp_on_count = len(self.lamp_group.get_lamps_that_are_on())

            if lamp_on_count > 0:
                ActionableNotification.send_notification(
                    self,
                    "Left house",
                    f"{lamp_on_count} lamps are still on. Turn them off?",
                    ActionableNotification.YES_NO_ACTION
                )
        elif old == "not_home" and new == "home":
            self.log("Got home")

    def on_event(self, event_name, data, kwargs) -> None:

        if data["action"] == 'Yes':
            self.log("Notification was answered with yes. Turning off all lamps.")
            self.lamp_group.turn_all_off()
