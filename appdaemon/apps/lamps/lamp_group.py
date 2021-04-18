from typing import List

import appdaemon.plugins.hass.hassapi as hass
from lamp_like import LampLike
from helpers import safe_get_app


class LampGroup(hass.Hass, LampLike):

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

    def turn_on(self, **kwargs) -> None:
        self.turn_all_on()

    def turn_off(self, **kwargs) -> None:
        self.turn_all_off()

    def set_brightness(self, brightness: int) -> None:
        self.log("Operation not supported")
        pass

    def toggle(self, **kwargs) -> None:
        if self.is_on():
            self.turn_off()
        else:
            self.turn_on()

    def is_on(self) -> bool:
        return self.any_lamp_is_on()

    def is_off(self) -> bool:
        return not self.is_on()
