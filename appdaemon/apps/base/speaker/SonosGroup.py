from typing import List, Dict, Any

import appdaemon.plugins.hass.hassapi as hass


class SonosGroup(hass.Hass):

    speakers: Dict[str, Any] = {}
    speaker_priority: List[str] = []

    def initialize(self) -> None:
        self.speaker_priority = self.args["speaker_priority"]
        self.log(f"Initialized {type(self)}")

    def register_speaker(self, speaker: Any) -> None:
        self.speakers[speaker.entity_id] = speaker

    def broadcast_message(self, message: str, language: str = "de"):
        for speaker in self.speakers.values():
            speaker.say(message, language)

    def join_all_as_group(self):
        leader = self._find_leader()

        for speaker in self.speakers.values():
            if speaker.entity_id != leader.entity_id:
                self.call_service("sonos/join", master=leader.entity_id, entity_id=speaker.entity_id)

    def unjoin_all_from_group(self):
        for speaker in self.speakers.values():
            self.unjoin_group(speaker)

    def join_group(self, speaker: Any) -> None:
        leader = self._find_leader(speaker.entity_id)
        if speaker.entity_id != leader.entity_id:
            self.call_service("sonos/join", master=leader.entity_id, entity_id=speaker.entity_id)

    def unjoin_group(self, speaker: Any) -> None:
        self.call_service("sonos/unjoin", entity_id=speaker.entity_id)

    def snapshot(self) -> None:
        self.call_service("sonos/snapshot")

    def restore_snapshot(self) -> None:
        self.call_service("sonos/restore")

    def someone_is_playing(self) -> bool:
        #print(f"Speakers: {self.speakers}")
        return len([1 for speaker in self.speakers.values() if speaker.is_playing()]) > 0

    def _find_leader(self, default_leader: str = None) -> Any:
        playing_speakers = [speaker for speaker in self.speakers.values() if speaker.is_playing()]
        if len(playing_speakers) != 0:
            return playing_speakers[0]
        else:
            if default_leader is None:
                return self.speakers[self.speaker_priority[0]]
            else:
                return default_leader
