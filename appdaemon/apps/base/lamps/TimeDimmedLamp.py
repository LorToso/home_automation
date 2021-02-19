from datetime import time, datetime
from typing import List

from attr import dataclass

from base.lamps.hue_lamp import HueLamp


@dataclass
class TimeWindowBrightness:
    start_time: time
    end_time: time
    brightness: int


class TimeDimmedLamp(HueLamp):
    default_brightness: int = HueLamp.MAX_BRIGHTNESS
    time_window_brightnesses: List[TimeWindowBrightness] = []

    def turn_on(self, **kwargs) -> None:
        # Brightness is explicitly specified. Let them
        if "brightness" in kwargs:
            super().turn_on(**kwargs)
        else:
            brightness = self.find_brightness_for_now()
            super().turn_on(brightness=brightness, **kwargs)

    def find_brightness_for_now(self) -> int:

        for window in self.time_window_brightnesses:
            now = datetime.now().time()
            if window.start_time <= now < window.end_time:
                return window.brightness

        return self.default_brightness
