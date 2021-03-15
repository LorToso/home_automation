from typing import List

import appdaemon.plugins.hass.hassapi as hass
from lamp_like import LampLike
from helpers import safe_get_app


class LampGroup(hass.Hass):

    lamps: List[LampLike]

    def initialize(self) -> None:
        self.lamps = [safe_get_app(self, lamp) for lamp in self.args["lamps"]]

    def any_lamp_is_on(self) -> bool:
        return any([lamp.is_on() for lamp in self.lamps])

    def get_lamps_that_are_on(self) -> List[LampLike]:
        return [lamp for lamp in self.lamps if lamp.is_on()]

    def turn_all_off(self):
        for lamp in self.lamps:
            lamp.turn_off()

    def turn_all_on(self):
        for lamp in self.lamps:
            lamp.turn_on()
