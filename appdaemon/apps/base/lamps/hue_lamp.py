from typing import Any, Dict

import appdaemon.plugins.hass.hassapi as hass

from base.lamps.lamp_like import LampLike


class HueLamp(hass.Hass, LampLike):
    MIN_BRIGHTNESS = 10
    MAX_BRIGHTNESS = 254
    BRIGHTNESS_DELTA = 20

    brightness: int = 0
    state: str = 'off'
    entity_id: str = "no_id"
    attributes: Dict[str, Any] = {}

    default_min_brightness: int = 50
    default_max_brightness: int = MAX_BRIGHTNESS

    def initialize(self) -> None:
        self.entity_id = self.args["entity_id"]

        if "default_min_brightness" in self.args:
            self.default_min_brightness = self.args["default_min_brightness"]
        if "default_max_brightness" in self.args:
            self.default_max_brightness = self.args["default_max_brightness"]
        if "attributes" in self.args:
            self.attributes = self.args["attributes"]

        self.listen_state(self.on_brightness_change, entity=self.entity_id, attribute="brightness", immediate=True)
        self.listen_state(self.on_state_change, entity=self.entity_id, immediate=True)

    def on_state_change(self, entity, attribute, old, new, kwargs):
        self.state = new
        self.log(f"State of {entity} is now {self.state}")

    def on_brightness_change(self, entity, attribute, old, new, kwargs):
        self.brightness = new
        self.log(f"Brightness of {entity} is now {self.brightness}")

    def turn_on(self, **kwargs) -> None:
        if not self.is_on() or "brightness" in kwargs:
            super().turn_on(self.entity_id, **self.attributes, **kwargs)

    def turn_off(self, **kwargs) -> None:
        if not self.is_off():
            super().turn_off(self.entity_id, **kwargs)

    def set_brightness(self, brightness: int) -> None:
        if brightness <= self.MIN_BRIGHTNESS:
            brightness = min(brightness, self.MIN_BRIGHTNESS)
        elif brightness >= self.MAX_BRIGHTNESS:
            brightness = max(brightness, self.MAX_BRIGHTNESS)
        self.turn_on(brightness=brightness)

    def reduce_brightness(self, delta: int = BRIGHTNESS_DELTA) -> None:
        self.set_brightness(self.brightness - delta)

    def increase_brightness(self, delta: int = BRIGHTNESS_DELTA) -> None:
        self.set_brightness(self.brightness + delta)

    def toggle(self, **kwargs) -> None:
        super().toggle(self.entity_id, **kwargs)

    def is_on(self) -> bool:
        return self.state == "on"

    def is_off(self) -> bool:
        return self.state == "off"

    def dimm_to_default_min(self) -> None:
        return self.set_brightness(self.default_min_brightness)

    def dimm_to_default_max(self) -> None:
        return self.set_brightness(self.default_max_brightness)
