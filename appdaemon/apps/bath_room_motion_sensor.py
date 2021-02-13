from typing import Optional

from base.input_boolean.input_boolean import InputBoolean
from base.lamps.HueLamp import HueLamp
from base.motion.MotionLightController import MotionLightController
from base.motion.AqaraMotionSensor import AqaraMotionSensor


class BathRoomMotionSensor(AqaraMotionSensor):
    activation_boolean: Optional[InputBoolean] = None
    motion_light_controller: MotionLightController

    def initialize(self) -> None:
        self.motion_light_controller = MotionLightController(self)
        self.activation_boolean = self.get_app(self.args["activation_boolean"])
        super().initialize()

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):

        if self.activation_boolean.is_off():
            self.log(f"Skipping action. {self.activation_boolean.entity_id} is in state {self.activation_boolean.state}")
            return

        self.motion_light_controller.on_motion_detected(old_motion_state, new_motion_state, state_duration)

