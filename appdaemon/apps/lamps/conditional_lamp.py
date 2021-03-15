from typing import List, Dict, Any, Tuple, Callable

from hue_lamp import HueLamp
from light_condition import parse_condition


class ConditionalLamp(HueLamp):

    conditions: List[Tuple[Callable[[], bool], Dict[str, Any]]] = []

    def initialize(self) -> None:
        super().initialize()
        self.conditions = []

        for condition_set in self.args["conditions"]:
            condition, attributes = parse_condition(condition_set)
            self.conditions.append((condition, attributes))

    def turn_on(self, **kwargs) -> None:
        # Brightness is explicitly specified. Let them
        if "brightness" in kwargs:
            super().turn_on(**kwargs)
        else:
            self.log(f"{self.conditions}")
            for condition, attributes in self.conditions:
                if condition():
                    super().turn_on(**attributes, **kwargs)
