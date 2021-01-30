from typing import Dict, Any

from base.input_boolean.input_boolean import InputBoolean
from base.notifier.ActionableNotification import ActionableNotification
from config import constants, strings

import appdaemon.plugins.hass.hassapi as hass


class GuestModeNotification(ActionableNotification):
    message = strings.guest_mode_activation_notification_message
    actions = [
        {
            "title": "Yes",
            "action": "Yes"
        },
        {
            "title": "No",
            "action": "No"
        },
    ]
    guest_mode_boolean: InputBoolean = None

    def initialize(self) -> None:
        self.guest_mode_boolean = InputBoolean(self, constants.guest_mode_activation_boolean)
        super().initialize()

    def on_receive(self, data: Dict[str, Any]):

        if data["action"] == "Yes":
            self.log("Guest mode activated")
            self.guest_mode_boolean.set_state(True)
        else:
            self.log("Guest mode deactivated")
            self.guest_mode_boolean.set_state(False)

    @staticmethod
    def send(controller: hass.Hass) -> None:
        ActionableNotification.send_notification(
            controller,
            message=GuestModeNotification.message,
            actions=GuestModeNotification.actions
        )



