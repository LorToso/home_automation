from typing import List, Union

import appdaemon.plugins.hass.hassapi as hass

from config import groups


class TTS:
    def __init__(self, controller: hass.Hass):
        self.controller = controller

    def broad_cast(self, message: str, language: str = "de") -> None:
        for entity_id in groups.speakers:
            self.say(entity_id, language, message)

    def say(self, entity_ids: Union[str, List[str]], message: str, language: str = "de"):
        if type(entity_ids) != list:
            entity_ids = [entity_ids]

        for entity_id in entity_ids:
            self.controller.call_service(
                service="tts/google_say",
                entity_id=entity_id,
                message=message,
                language=language
            )
