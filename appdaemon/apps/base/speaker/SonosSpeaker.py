from typing import Dict, Any

import appdaemon.plugins.hass.hassapi as hass

from base.tts.TTS import TTS


class SonosSpeaker:

    def __init__(self,
                 controller: hass.Hass,
                 speaker_entity_id: str,
                 # reset_volume_timeout_sec: int = 3600,
                 # default_volume: float = 0.1
                 ):
        self.controller: hass.Hass = controller
        self.speaker_entity_id: str = speaker_entity_id
        self.state: str = "paused"

        self.controller.log(f'listening to state for entity {self.speaker_entity_id}')
        self.controller.listen_state(self.on_state, entity=self.speaker_entity_id, immediate=True)

        # self.reset_volume_timeout_sec = reset_volume_timeout_sec
        # self.default_volume = default_volume

    def on_state(self, entity, attribute, old, new, kwargs) -> None:
        # state_duration = kwargs['state_duration']
        self.state = new

        # if (new == "paused" or new == "stopped") and state_duration == self.reset_volume_timeout_sec:
        #    self.reset_volume()

        # pass

    # def reset_volume(self):
    #    self.set_volume(self.default_volume)

    def set_volume(self, volume: float):
        self.controller.set_state(self.speaker_entity_id,
                                  volume_level=volume)

    def say(self, message: str, language: str = "de"):
        TTS(self.controller).say(
            self.speaker_entity_id,
            message,
            language
        )

    def is_playing(self) -> bool:
        return self.state == "playing"

    def join_group(self) -> bool:
        # TODP
        pass
