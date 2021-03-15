from abc import abstractmethod
from typing import Any, Dict, List

import appdaemon.plugins.hass.hassapi as hass


class ActionableNotification(hass.Hass):

    def initialize(self) -> None:
        self.listen_event(self.on_event, "mobile_app_notification_action")
        self.log(f"Initialized {type(self)}")

    def on_event(self, event_name: str, data: Dict[str, Any], **kwargs: Dict[str, Any]) -> None:
        return self.on_receive(data)

    @staticmethod
    def send_notification(controller: hass.Hass, message: str, actions: List[Dict[str, str]]) -> None:
        controller.log(f"Sending actionable phone notification with message [{message}]")
        controller.notify(
            message=message,
            data={
                "actions": actions
            }
        )

    @abstractmethod
    def on_receive(self, data: Dict[str, Any]):
        pass
