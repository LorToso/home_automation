from typing import Dict, Any

import appdaemon.plugins.hass.hassapi as hass

from base.speaker.SonosSpeaker import SonosSpeaker
from base.tts.TTS import TTS


class DefaultSonosSpeaker(SonosSpeaker):

    default_volume: float = 0.2
    default_volume_timeout_sec: int = 3600

    def initialize(self):
        self.default_volume = self.args["default_volume"]
        self.listen_state(self.on_pause_timeout, entity=self.entity_id, duration=self.default_volume_timeout_sec, new="paused")
        super().initialize()

    def on_pause_timeout(self):
        self.set_volume(self.default_volume)

    def say(self, message: str, language: str = "de"):
        self.snapshot()
        super().say(message, language)
        self.restore_snapshot()

