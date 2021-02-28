from datetime import datetime
from typing import Dict, Any, List

import appdaemon.plugins.hass.hassapi as hass

from base.helpers.helpers import safe_get_app
from base.speaker.sonos_group import SonosGroup
from base.tts.TTS import TTS


class SonosSpeaker(hass.Hass):

    entity_id: str = ""
    state: str = "off"
    volume: float = 0
    speaker_group_str: List[str] = []
    speaker_group: SonosGroup = None

    def initialize(self) -> None:
        self.entity_id = self.args["entity_id"]
        self.speaker_group = safe_get_app(self, self.args["speaker_group"])
        self.speaker_group_str = [self.entity_id]

        self.log(f'listening to state for entity {self.entity_id}')
        self.listen_state(self.on_state, entity=self.entity_id, immediate=True)
        self.listen_state(self.on_state, entity=self.entity_id, immediate=True, attribute="volume")
        self.listen_state(self.on_state, entity=self.entity_id, immediate=True, attribute="sonos_group")

        self.speaker_group.register_speaker(self)

        self.run_minutely(self.on_interval, datetime.now())

    def on_interval(self, kwargs: Dict[str, Any]) -> None:
        self.state = self.get_state(entity_id=self.entity_id)
        self.volume = self.get_state(entity_id=self.entity_id, attribute="volume")
        self.speaker_group_str = self.get_state(entity_id=self.entity_id, attribute="sonos_group")
        if self.speaker_group_str is None:
            self.speaker_group_str = [self.entity_id]

    def on_state(self, entity, attribute, old, new, kwargs) -> None:

        if attribute is None:
            self.log(f"New state: {new}")
            self.state = new
            self.on_state_changed(old, new)
        elif attribute == "volume_level":
            self.log(f"New volume: {new}")
            self.volume = new
            self.on_volume_changed(old, new)
        elif attribute == "sonos_group":
            self.log(f"New sonos_group: {new}")
            self.speaker_group_str = new
            if new is None:
                new = [self.entity_id]
            if len(new) > 1:
                self.log(f"Joined group with leader {self.speaker_group_str[0]}")
                self.on_group_joined()
            else:
                self.log(f"Unjoined group")
                self.on_group_unjoined()

    def on_state_changed(self, old_state: str, new_state: str) -> None:
        pass

    def on_volume_changed(self, old_volume: float, new_state: float) -> None:
        pass

    def on_group_joined(self) -> None:
        pass

    def on_group_unjoined(self) -> None:
        pass

    def set_volume(self, volume: float):
        self.call_service("media_player/volume_set", entity_id=self.entity_id, volume_level=volume)

    def say(self, message: str, language: str = "de"):
        TTS(self).say(
            self.entity_id,
            message,
            language
        )

    def is_playing(self) -> bool:
        return self.state == "playing"

    def is_group_leader(self) -> bool:
        return self.speaker_group_str is None or self.speaker_group_str[0] == self.entity_id

    def is_in_group(self) -> bool:
        self.log(f"self.speaker_group_str = {self.speaker_group_str}")
        return self.speaker_group_str is not None and len(self.speaker_group_str) > 1

    def join_group(self) -> None:
        if self.is_in_group():
            return
        self.log("Joining group")
        self.speaker_group.join_group(self)

    def unjoin_group(self) -> None:
        if not self.is_in_group():
            return
        self.log("Unjoining group")
        self.speaker_group.unjoin_group(self)

    def snapshot(self) -> None:
        self.call_service("sonos/snapshot", entity_id=self.entity_id, with_group=True)

    def restore_snapshot(self) -> None:
        self.call_service("sonos/restore", entity_id=self.entity_id, with_group=True)

    def pause(self):
        self.call_service("media_player.media_pause", entity_id=self.entity_id)

    def play(self):
        self.call_service("media_player.media_play", entity_id=self.entity_id)
