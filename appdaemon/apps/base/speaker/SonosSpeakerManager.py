from base.speaker.SonosSpeaker import SonosSpeaker
import appdaemon.plugins.hass.hassapi as hass
from config import groups


class SonosSpeakerManager:

    def __init__(self, controller: hass.Hass):
        self.speakers = {entity_id: SonosSpeaker(controller, entity_id) for entity_id in groups.speakers}

    #def