from typing import Dict, Any

import appdaemon.plugins.hass.hassapi as hass

from base.speaker.SonosSpeaker import SonosSpeaker
from base.tts.TTS import TTS


class DefaultSonosSpeaker(SonosSpeaker):

    def initialize(self):

        super().initialize()

    pass
