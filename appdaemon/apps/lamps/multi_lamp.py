from typing import Any, Dict, List

import appdaemon.plugins.hass.hassapi as hass

from lamp_like import LampLike

from hue_lamp import HueLamp


class MultiLamp(hass.Hass, LampLike):

    brightness: Dict[str, int] = {}
    state: Dict[str, str] = {}
    entity_ids: List[str] = []
    attributes: Dict[str, Any] = {}

    default_min_brightness: int = 50
    default_max_brightness: int = HueLamp.MAX_BRIGHTNESS

    def initialize(self) -> None:
        self.entity_ids = self.args["entity_ids"]
        self.state = {}
        self.brightness = {}

        if "default_min_brightness" in self.args:
            self.default_min_brightness = self.args["default_min_brightness"]
        if "default_max_brightness" in self.args:
            self.default_max_brightness = self.args["default_max_brightness"]
        if "attributes" in self.args:
            self.attributes = self.args["attributes"]

        for entity_id in self.entity_ids:
            self.state[entity_id] = "off"
            self.brightness[entity_id] = 0
            self.listen_state(self.on_brightness_change, entity=entity_id, attribute="brightness", immediate=True)
            self.listen_state(self.on_state_change, entity=entity_id, immediate=True)

    def on_state_change(self, entity, attribute, old, new, kwargs):
        self.state[entity] = new
        self.log(f"State of {entity} is now {new}")

    def on_brightness_change(self, entity, attribute, old, new, kwargs):
        self.brightness[entity] = new
        self.log(f"Brightness of {entity} is now {new}")

    def turn_on(self, **kwargs) -> None:
        if not self.is_on() or "brightness" in kwargs:
            for entity_id in self.entity_ids:
                super().turn_on(entity_id, **self.attributes, **kwargs)

    def turn_off(self, **kwargs) -> None:
        if not self.is_off():
            for entity_id in self.entity_ids:
                super().turn_off(entity_id, **kwargs)

    def set_brightness(self, brightness: int) -> None:
        if brightness <= HueLamp.MIN_BRIGHTNESS:
            brightness = HueLamp.MIN_BRIGHTNESS
        elif brightness >= HueLamp.MAX_BRIGHTNESS:
            brightness = HueLamp.MAX_BRIGHTNESS
        self.turn_on(brightness=brightness)

    def reduce_brightness(self, delta: int = HueLamp.BRIGHTNESS_DELTA) -> None:
        self.set_brightness(self.brightness[self.entity_ids[0]] - delta)

    def increase_brightness(self, delta: int = HueLamp.BRIGHTNESS_DELTA) -> None:
        self.set_brightness(self.brightness[self.entity_ids[0]] + delta)

    def toggle(self, **kwargs) -> None:
        if self.is_on():
            self.turn_off(**kwargs)
        else:
            self.turn_on(**kwargs)

    def is_on(self) -> bool:
        return any([state == "on" for state in self.state.values()])

    def is_off(self) -> bool:
        return all([state == "off" for state in self.state.values()])

    def dimm_to_default_min(self) -> None:
        return self.set_brightness(self.default_min_brightness)

    def dimm_to_default_max(self) -> None:
        return self.set_brightness(self.default_max_brightness)
