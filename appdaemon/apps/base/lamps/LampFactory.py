from datetime import time

import constants
from base.lamps.HueLamp import HueLamp
import appdaemon.plugins.hass.hassapi as hass

from base.lamps.TimeDimmedLamp import TimeDimmedLamp, TimeWindowBrightness


class LampFactory:

    bath_room_time_windows = [
        TimeWindowBrightness(
            start_time=time(hour=0, minute=0),
            end_time=time(hour=7, minute=0),
            brightness=50  # 20%
        ),
        TimeWindowBrightness(
            start_time=time(hour=7, minute=0),
            end_time=time(hour=10, minute=0),
            brightness=125  # 50%
        ),
        TimeWindowBrightness(
            start_time=time(hour=10, minute=0),
            end_time=time(hour=20, minute=0),
            brightness=225  # 90%
        ),
        TimeWindowBrightness(
            start_time=time(hour=20, minute=0),
            end_time=time(hour=23, minute=59, second=59),
            brightness=125  # 50%
        ),
    ]

    @staticmethod
    def build_lamp(controller: hass.Hass, entity_id: str) -> HueLamp:

        if entity_id == constants.bath_room_lamp_id:
            return TimeDimmedLamp(controller, entity_id, LampFactory.bath_room_time_windows)

        return HueLamp(controller, entity_id)

