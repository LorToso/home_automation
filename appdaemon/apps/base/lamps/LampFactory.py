from base.lamps.HueLamp import HueLamp
import appdaemon.plugins.hass.hassapi as hass


class LampFactory:

    @staticmethod
    def build_lamp(controller: hass.Hass, entity_id: str) -> HueLamp:
        return HueLamp(controller, entity_id)
