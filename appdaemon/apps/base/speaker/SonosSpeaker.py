from typing import Optional

import appdaemon.plugins.hass.hassapi as hass

from base.speaker.SonosGroup import SonosGroup
from base.tts.TTS import TTS


class SonosSpeaker(hass.Hass):

    entity_id: str = ""
    state: str = "off"
    volume: float = 0
    speaker_group: Optional[SonosGroup] = None

    def initialize(self) -> None:
        self.log(f'listening to state for entity {self.entity_id}')
        self.entity_id = self.args["entity_id"]
        self.speaker_group = self.get_app(self.args["speaker_group_app_name"])

        self.listen_state(self.on_state, entity=self.entity_id, immediate=True)
        self.listen_state(self.on_state, entity=self.entity_id, immediate=True, attribute="volume")

        self.speaker_group.register_speaker(self)

        self.log(f"Initialized {type(self)}")

    def on_state(self, entity, attribute, old, new, kwargs) -> None:
        # state_duration = kwargs['state_duration']
        if attribute == "state":
            self.state = new
            self.on_state_changed(old, new)
        elif attribute == "volume_level":
            self.volume = new
            self.on_volume_changed(old, new)

    def on_state_changed(self, old_state: str, new_state: str) -> None:
        pass

    def on_volume_changed(self, old_volume: float, new_state: float) -> None:
        pass

    def set_volume(self, volume: float):
        self.log(f"self.call_service('media_player.volume_set', state={self.state}, volume_level={volume})")
        self.call_service("media_player/volume_set", entity_id=self.entity_id, volume_level=volume)
        #self.set_state(self.entity_id, state=self.state, volume_level=volume)

    def say(self, message: str, language: str = "de"):
        TTS(self).say(
            self.entity_id,
            message,
            language
        )

    def is_playing(self) -> bool:
        return self.state == "playing"

    def join_group(self) -> None:
        self.speaker_group.join_group(self)

    def unjoin_group(self) -> None:
        self.speaker_group.unjoin_group(self)

    def snapshot(self) -> None:
        self.call_service("sonos.snapshot", entity_id=self.entity_id, with_group=True)

    def restore_snapshot(self) -> None:
        self.call_service("sonos.restore", entity_id=self.entity_id, with_group=True)

    def pause(self):
        self.call_service("media_player.media_pause", entity_id=self.entity_id)

    def play(self):
        self.call_service("media_player.media_play", entity_id=self.entity_id)
