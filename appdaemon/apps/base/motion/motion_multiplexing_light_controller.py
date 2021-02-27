from datetime import datetime
from typing import List, Dict, Callable, Tuple

from base.helpers.helpers import safe_get_app
from base.lamps.hue_lamp import HueLamp
from base.lamps.lamp_like import LampLike
from base.lamps.lamp_multiplexer import LampMultiplexer
from base.motion.motion_light_controller import MotionLightController


class MotionMultiplexingLightController(MotionLightController):

    def create_lamp(self) -> LampLike:
        lamp_multiplexer = LampMultiplexer(self)

        lamps_and_conditions: List[Dict[str, str]] = self.args["lamps"]

        for lamp_and_condition in lamps_and_conditions:
            lamp, condition = self.parse_lamp(lamp_and_condition)
            lamp_multiplexer.add_lamp(lamp, condition)

        return lamp_multiplexer

    def parse_lamp(self, properties: Dict[str, str]) -> Tuple[HueLamp, Callable[[], bool]]:

        lamp: HueLamp = safe_get_app(self, properties["app_name"])

        if "start_time" in properties and "end_time" in properties:
            start_time = datetime.strptime(properties["start_time"], "%H:%M:%S").time()
            end_time = datetime.strptime(properties["end_time"], "%H:%M:%S").time()

            return lamp, lambda: start_time <= datetime.now().time() < end_time

        return lamp, lambda: True
