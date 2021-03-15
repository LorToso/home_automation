from typing import Callable, List, Tuple, Dict, Any

import appdaemon.plugins.hass.hassapi as hass

from lamp_like import LampLike


class LampMultiplexer(LampLike):

    def __init__(self, controller: hass.Hass):
        self.controller = controller
        self.lamps_and_conditions: List[Tuple[LampLike, Callable[[], bool], Dict[str, Any]]] = []
        pass

    def add_lamp(self, lamp: LampLike, attributes: Dict[str, Any], condition: Callable[[], bool] = lambda: True) -> None:
        self.lamps_and_conditions.append((lamp, condition, attributes))

    def turn_on(self, **kwargs) -> None:
        self.controller.log("trying to turn on")
        for lamp, condition, attributes in self.lamps_and_conditions:
            self.controller.log(f"{lamp} --- {condition} --- {attributes}")
            if condition():
                self.controller.log(f"lamp {lamp} condition true")
                lamp.turn_on(**attributes, **kwargs)
            else:
                self.controller.log(f"lamp {lamp} condition false")

    def turn_off(self, **kwargs) -> None:
        for lamp, _, _ in self.lamps_and_conditions:
            lamp.turn_off(**kwargs)

    def set_brightness(self, brightness: int) -> None:
        for lamp, condition, _ in self.lamps_and_conditions:
            if condition():
                lamp.set_brightness(brightness)

    def toggle(self, **kwargs) -> None:
        for lamp, condition, _ in self.lamps_and_conditions:
            if condition():
                lamp.toggle(**kwargs)

    def is_on(self) -> bool:
        return any([lamp.is_on() for lamp, _, _ in self.lamps_and_conditions])

    def is_off(self) -> bool:
        return all([lamp.is_off() for lamp, _, _ in self.lamps_and_conditions])
