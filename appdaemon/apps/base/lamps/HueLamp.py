from typing import List

import appdaemon.plugins.hass.hassapi as hass

MIN_BRIGHTNESS = 10
MAX_BRIGHTNESS = 254
BRIGHTNESS_DELTA = 20


class Colors:
    # R G B BRIGHTNESS
    RED = [255, 56, 57, 254]

    WARM_WHITE = [255, 53, 53]

class HueLamp:
    brightness = 0
    state = 'off'

    def __init__(self, controller: hass.Hass, device_id: str):

        self.controller = controller
        self.device_id = device_id

        self.controller.listen_state(self.on_brightness_change, entity=device_id, attribute="brightness", immediate=True)
        self.controller.listen_state(self.on_state_change, entity=device_id, immediate=True)

    def on_state_change(self, entity, attribute, old, new, kwargs):
        self.state = new
        self.controller.log(f"State of {entity} is now {self.state}")

    def on_brightness_change(self, entity, attribute, old, new, kwargs):
        self.brightness = new
        self.controller.log(f"Brightness of {entity} is now {self.brightness}")

    def turn_on(self, **kwargs) -> None:
        self.controller.turn_on(self.device_id, **kwargs)

    def turn_off(self) -> None:
        self.controller.turn_off(self.device_id)

    def set_brightness(self, brightness: int) -> None:
        if brightness <= MIN_BRIGHTNESS:
            pass
        elif brightness >= MAX_BRIGHTNESS:
            self.turn_on(brightness=MAX_BRIGHTNESS)
        else:
            self.turn_on(brightness=brightness)

    def reduce_brightness(self, delta: int = BRIGHTNESS_DELTA) -> None:
        self.set_brightness(self.brightness - delta)

    def increase_brightness(self, delta: int = BRIGHTNESS_DELTA) -> None:
        self.set_brightness(self.brightness + delta)

    def toggle(self) -> None:
        self.controller.toggle(self.device_id)

    def is_on(self) -> bool:
        return self.state == "on"


