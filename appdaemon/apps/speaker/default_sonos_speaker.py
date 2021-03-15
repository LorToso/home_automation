from typing import Dict, Any

from sonos_speaker import SonosSpeaker


class DefaultSonosSpeaker(SonosSpeaker):

    default_volume: float = 0.2
    default_volume_timeout_sec: int = 3600

    def initialize(self):
        super().initialize()
        self.default_volume = self.args["default_volume"]
        self.listen_state(self.on_pause_timeout,
                          entity=self.entity_id,
                          duration=self.default_volume_timeout_sec,
                          immediate=True,
                          new="paused")
        self.listen_state(self.on_pause_timeout,
                          entity=self.entity_id,
                          duration=self.default_volume_timeout_sec,
                          immediate=True,
                          new="idle")

    def on_pause_timeout(self, entity: str, attribute: str, old: str, new: str, kwargs: Dict[str, Any]) -> None:
        self.set_volume(self.default_volume)
        self.unjoin_group()

    def say(self, message: str, language: str = "de") -> None:

        was_in_group = self.is_in_group()

        if was_in_group:
            self.unjoin_group()

        super().say(message, language)

        if was_in_group:
            self.join_group()
