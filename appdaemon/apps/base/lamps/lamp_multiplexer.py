from typing import Callable, List, Tuple

import appdaemon.plugins.hass.hassapi as hass

from base.lamps.lamp_like import LampLike


class LampMultiplexer(LampLike):

    def __init__(self, controller: hass.Hass):
        self.controller = controller
        self.lamps_and_conditions: List[Tuple[LampLike, Callable[[], bool]]] = []
        pass

    def add_lamp(self, lamp: LampLike, condition: Callable[[], bool] = lambda: True) -> None:
        self.lamps_and_conditions.append((lamp, condition))

    def turn_on(self, **kwargs) -> None:
        self.controller.log("trying to turn on")
        for lamp, condition in self.lamps_and_conditions:
            if condition():
                self.controller.log(f"lamp {lamp.entity_id} condition true")
                lamp.turn_on(**kwargs)
            else:
                self.controller.log(f"lamp {lamp.entity_id} condition false")

    def turn_off(self, **kwargs) -> None:
        for lamp, condition in self.lamps_and_conditions:
            lamp.turn_off(**kwargs)

    def set_brightness(self, brightness: int) -> None:
        for lamp, condition in self.lamps_and_conditions:
            if condition():
                lamp.set_brightness(brightness)

    def toggle(self, **kwargs) -> None:
        for lamp, condition in self.lamps_and_conditions:
            if condition():
                lamp.toggle(**kwargs)

    def is_on(self) -> bool:
        return any([lamp.is_on() for lamp, _ in self.lamps_and_conditions])

    def is_off(self) -> bool:
        return all([lamp.is_off() for lamp, _ in self.lamps_and_conditions])
