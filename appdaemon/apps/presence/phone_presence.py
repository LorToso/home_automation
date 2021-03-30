import appdaemon.plugins.hass.hassapi as hass
from lamp_group import LampGroup

from helpers import safe_get_app
from notifier.actionable_notification import ActionableNotification


class PhonePresence(hass.Hass):

    lamp_group: LampGroup

    def initialize(self) -> None:
        self.lamp_group = safe_get_app(self, self.args["lamp_group"])

        self.listen_state(self.on_state, entity=self.args["phone_tracker_id"], immediate=True)
        self.listen_state(self.on_phone_wifi, entity=self.args["phone_wifi_sensor_id"], immediate=True)
        self.listen_event(self.on_event, event="mobile_app_notification_action")

    def on_phone_wifi(self, entity, attribute, old, new, kwargs) -> None:

        if new == "TearDownThisWLAN":
            self.on_got_home()
        else:
            self.on_left_home()

    def on_state(self, entity, attribute, old, new, kwargs) -> None:

        if old == "home" and new == "not_home":
            self.on_left_home()
        elif old == "not_home" and new == "home":
            self.on_got_home()

    def on_left_home(self):
        self.log("Left home")
        self.turn_off(self.args["phone_presence_boolean"])

        lamp_on_count = len(self.lamp_group.get_lamps_that_are_on())
        if lamp_on_count > 0:
            ActionableNotification.send_notification(
                self,
                "Left house",
                f"{lamp_on_count} lamps are still on. Turn them off?",
                ActionableNotification.YES_NO_ACTION
            )

    def on_got_home(self):
        self.log("Got home")
        self.turn_on(self.args["phone_presence_boolean"])

    def on_event(self, event_name, data, kwargs) -> None:
        if data["action"] == 'Yes':
            self.log("Notification was answered with yes. Turning off all lamps.")
            self.lamp_group.turn_all_off()

