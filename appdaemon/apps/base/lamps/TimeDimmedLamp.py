from datetime import time, datetime
from typing import List

import appdaemon.plugins.hass.hassapi as hass
from attr import dataclass

from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS


@dataclass
class TimeWindowBrightness:
    start_time: time
    end_time: time
    brightness: int


class TimeDimmedLamp(HueLamp):

    def __init__(self, controller: hass.Hass, entity_id: str, time_window_brightnesses: List[TimeWindowBrightness], default_brightness=MAX_BRIGHTNESS):
        self.controller = controller
        self.entity_id = entity_id
        self.time_window_brightnesses = time_window_brightnesses
        self.default_brightness = default_brightness

        super().__init__(controller, entity_id)

    def turn_on(self, **kwargs) -> None:
        # Brightness is explicitly specified. Let them
        if "brightness" in kwargs:
            super().turn_on(**kwargs)
        else:
            brightness = self.find_brightness_for_now()
            self.controller.turn_on(self.entity_id, brightness=brightness, **kwargs)

    def find_brightness_for_now(self) -> int:

        for window in self.time_window_brightnesses:
            now = datetime.now().time()
            if window.start_time <= now < window.end_time:
                return window.brightness

        return self.default_brightness
