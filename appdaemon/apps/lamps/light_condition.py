from datetime import datetime
from typing import Dict, Callable, Tuple, Any

ignored_attributes = ["start_time", "end_time", "app_name"]


def parse_condition(properties: Dict[str, Any]) -> Tuple[Callable[[], bool], Dict[str, Any]]:

    matcher = lambda: True

    if "start_time" in properties and "end_time" in properties:
        start_time = datetime.strptime(properties["start_time"], "%H:%M:%S").time()
        end_time = datetime.strptime(properties["end_time"], "%H:%M:%S").time()

        matcher = lambda: start_time <= datetime.now().time() < end_time

    for attribute in ignored_attributes:
        properties.pop(attribute, None)

    return matcher, properties
