from datetime import time, datetime
from typing import List

import appdaemon.plugins.hass.hassapi as hass
from attr import dataclass

from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS


class NightStandLamp(HueLamp):

    AVAILABLE_COLORS = {
        "red": {
            "color_temp": 499,
            "brightness": 254
        },
        "warm_white": {
            "color_temp": 333,
            "brightness": 254
        },
    }

    def __init__(self, controller: hass.Hass, entity_id: str):
        self.controller = controller
        self.entity_id = entity_id

        super().__init__(controller, entity_id)

    def set_color(self, color: str) -> None:
        self.controller.log(f"setting color {color} to lamp {self.entity_id}")
        self.turn_on(**self.AVAILABLE_COLORS[color])
