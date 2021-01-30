from typing import Dict, Any

import appdaemon.plugins.hass.hassapi as hass

import config.strings
from config import constants
from base.tts.TTS import TTS


class ActionableNotificationHandler(hass.Hass):

    def initialize(self) -> None:
        self.log(f"Listening to 'mobile_app_notification_action' events")

        self.listen_event(self.on_event, event_name="mobile_app_notification_action", immediate=False)
        self.log(f"Done initializing {type(self)}")

    def on_event(self, event_name: str, data: Dict[str, Any], kwargs: Dict[str, Any]) -> None:
        pass
