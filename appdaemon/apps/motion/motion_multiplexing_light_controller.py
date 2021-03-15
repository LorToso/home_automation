from typing import List, Dict

from helpers import safe_get_app
from lamp_like import LampLike
from lamp_multiplexer import LampMultiplexer
from conditional_lamp import parse_condition
from motion_light_controller import MotionLightController


class MotionMultiplexingLightController(MotionLightController):

    def create_lamp(self) -> LampLike:
        lamp_multiplexer = LampMultiplexer(self)

        lamps_and_conditions: List[Dict[str, str]] = self.args["lamps"]

        for lamp_and_condition in lamps_and_conditions:
            lamp = safe_get_app(self, lamp_and_condition["app_name"])
            condition, attributes = parse_condition(lamp_and_condition)
            lamp_multiplexer.add_lamp(lamp, attributes, condition)

        return lamp_multiplexer
