from typing import Any, Dict
from helpers import safe_get_app
import appdaemon.plugins.hass.hassapi as hass

from lamp_like import LampLike

from lamp_multiplexer import LampMultiplexer


class LampMultiplexerApp(hass.Hass, LampLike):
    BRIGHTNESS_DELTA = 20
    MIN_BRIGHTNESS = 10
    MAX_BRIGHTNESS = 254

    default_min_brightness: int = 50
    default_max_brightness: int = MAX_BRIGHTNESS
    attributes: Dict[str, Any] = {}

    lamp_multiplexer: LampMultiplexer

    def initialize(self) -> None:
        self.lamp_multiplexer = LampMultiplexer(self)

        if "default_min_brightness" in self.args:
            self.default_min_brightness = self.args["default_min_brightness"]
        if "default_max_brightness" in self.args:
            self.default_max_brightness = self.args["default_max_brightness"]
        if "attributes" in self.args:
            self.attributes = self.args["attributes"]

        lamps = self.args["lamps"]
        for lamp in lamps:
            self.lamp_multiplexer.add_lamp(safe_get_app(self, lamp), self.attributes, lambda: True)

    def turn_on(self, **kwargs) -> None:
        self.lamp_multiplexer.turn_on(**kwargs)

    def turn_off(self, **kwargs) -> None:
        self.lamp_multiplexer.turn_off(**kwargs)

    def set_brightness(self, brightness: int) -> None:
        self.turn_on(brightness=brightness)

    def reduce_brightness(self, delta: int = BRIGHTNESS_DELTA) -> None:
        self.set_brightness(self.brightness - delta)

    def increase_brightness(self, delta: int = BRIGHTNESS_DELTA) -> None:
        self.set_brightness(self.brightness + delta)

    def toggle(self, **kwargs) -> None:
        if self.lamp_multiplexer.is_on():
            self.lamp_multiplexer.turn_off()
        else:
            self.lamp_multiplexer.turn_on()

    def is_on(self) -> bool:
        return self.lamp_multiplexer.is_on()

    def is_off(self) -> bool:
        return self.lamp_multiplexer.is_off()

    def dimm_to_default_min(self) -> None:
        return self.set_brightness(self.default_min_brightness)

    def dimm_to_default_max(self) -> None:
        return self.set_brightness(self.default_max_brightness)
