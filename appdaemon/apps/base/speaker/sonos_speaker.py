from typing import Optional

import appdaemon.plugins.hass.hassapi as hass

from base.helpers.helpers import safe_get_app
from base.speaker.sonos_group import SonosGroup
from base.tts.TTS import TTS


class SonosSpeaker(hass.Hass):

    entity_id: str = ""
    state: str = "off"
    volume: float = 0
    is_in_group: bool = False
    speaker_group_leader: str = ""
    speaker_group: SonosGroup = None

    def initialize(self) -> None:
        self.entity_id = self.args["entity_id"]
        self.speaker_group = safe_get_app(self, self.args["speaker_group"])
        self.speaker_group_leader = self.args["entity_id"]

        self.log(f'listening to state for entity {self.entity_id}')
        self.listen_state(self.on_state, entity=self.entity_id, immediate=True)
        self.listen_state(self.on_state, entity=self.entity_id, immediate=True, attribute="volume")
        self.listen_state(self.on_state, entity=self.entity_id, immediate=True, attribute="sonos_group")

        self.speaker_group.register_speaker(self)

        self.log(f"Initialized {type(self)}")

    def on_state(self, entity, attribute, old, new, kwargs) -> None:

        if attribute is None:
            self.log(f"New state: {new}")
            self.state = new
            self.on_state_changed(old, new)
        elif attribute == "volume_level":
            self.volume = new
            self.on_volume_changed(old, new)
        elif attribute == "sonos_group":
            if new is None:
                new = [self.entity_id]
            self.speaker_group_leader = new[0]
            if len(new) > 1:
                self.is_in_group = True
                self.log(f"Joined group with leader {self.speaker_group_leader}")
                self.on_group_joined()
            else:
                self.is_in_group = False
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
        return self.speaker_group_leader == self.entity_id

    def join_group(self) -> None:
        if self.is_in_group:
            return
        self.log("Joining group")
        self.speaker_group.join_group(self)

    def unjoin_group(self) -> None:
        if not self.is_in_group:
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
