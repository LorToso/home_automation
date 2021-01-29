from abc import abstractmethod
from typing import Any, Dict

import appdaemon.plugins.hass.hassapi as hass


class AqaraMotionSensor(hass.Hass):

    motion_entity_id: str = "0"
    durations = []
    motion_state = 0

    def initialize(self) -> None:
        for duration in set(self.durations):
            self.log(f"listening to state_changes for id {self.motion_entity_id} with duration {duration}")
            self.listen_state(
                self.on_state,
                entity=self.motion_entity_id,
                immediate=True,
                duration=duration,
                state_duration=duration
            )
        self.log(f"{type(self)} initialised with sensor_entity_id ({self.motion_entity_id})")

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
