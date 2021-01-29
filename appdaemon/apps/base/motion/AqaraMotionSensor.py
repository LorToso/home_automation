from abc import abstractmethod
from typing import Any, Dict
import appdaemon.plugins.hass.hassapi as hass
from appdaemon.appdaemon import AppDaemon


class AqaraMotionSensor(hass.Hass):

    sensor_entity_id: str = "0"
    duration = None
    motion_state = 0

    def initialize(self) -> None:
        if self.duration is None:
            self.log(f'listening to state_changes for id {self.sensor_entity_id}')
            self.log(f"duration is None")
            self.listen_state(self.on_state, entity=self.sensor_entity_id, immediate=True)
        else:
            self.log(f"listening to state_changes for id {self.sensor_entity_id} with duration {self.duration}")
            self.listen_state(
                self.on_state,
                entity=self.sensor_entity_id,
                immediate=True,
                duration=self.duration,
                state_duration=self.duration
            )
            self.log(f"listening to state_changes for id {self.sensor_entity_id} with duration {0}")
            self.listen_state(
                self.on_state,
                entity=self.sensor_entity_id,
                immediate=False,
                state_duration=0
            )

    def on_state(self, entity, attribute, old, new, kwargs: Dict[str, Any]) -> None:
        state_duration = kwargs['state_duration']
        self.log(f"Received state changed for entity {entity} from ({old}) to ({new}) with duration parameter ({state_duration})")
        self.motion_state = new

        if old is None:
            old = "off"

        self.on_motion_detected(old, new, state_duration)

    @abstractmethod
    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        pass
