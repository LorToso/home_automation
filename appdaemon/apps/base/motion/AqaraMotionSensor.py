from abc import abstractmethod
from typing import Any, Dict, List, Set

import appdaemon.plugins.hass.hassapi as hass


class AqaraMotionSensor(hass.Hass):

    motion_entity_id: str = "0"
    motion_state = "off"
    listened_durations: Set[int] = {}

    def initialize(self) -> None:
        self.log(f"{type(self)} initialised with sensor_entity_id ({self.motion_entity_id})")

    def listen_to(self, duration: int, **kwargs):

        if duration in self.listened_durations:
            return
        else:
            self.listened_durations += duration

        self.log(f"listening to state_changes for id {self.motion_entity_id} with duration {duration}")
        self.listen_state(
            self.on_state,
            entity=self.motion_entity_id,
            immediate=True,
            duration=duration,
            state_duration=duration,
            **kwargs
        )

    def on_state(self, entity, attribute, old, new, kwargs: Dict[str, Any]) -> None:
        state_duration = kwargs['state_duration']
        #self.log(f"Received state changed for entity {entity} from ({old}) to ({new}) with duration parameter ({state_duration})")
        self.motion_state = new

        if old is None:
            old = "off"

        self.on_motion_detected(old, new, state_duration)

    @abstractmethod
    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        pass
