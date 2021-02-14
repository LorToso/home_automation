from typing import Optional

from base.input_boolean.input_boolean import InputBoolean
from base.motion.AqaraMotionSensor import AqaraMotionSensor
from base.motion.MotionLightController import MotionLightController
from base.motion.MusicFollowingController import MusicFollowingController


class BathRoomMotionSensor(AqaraMotionSensor):
    activation_boolean: Optional[InputBoolean] = None
    motion_light_controller: MotionLightController
    music_following_controller: MusicFollowingController

    def initialize(self) -> None:
        super().initialize()
        self.motion_light_controller = MotionLightController(self)
        self.music_following_controller = MusicFollowingController(self)
        self.activation_boolean = self.get_app(self.args["activation_boolean"])

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):

        if self.activation_boolean.is_off():
            self.log(f"Skipping action. {self.activation_boolean.entity_id} is in state {self.activation_boolean.state}")
            return

        self.motion_light_controller.on_motion_detected(old_motion_state, new_motion_state, state_duration)
        self.music_following_controller.on_motion_detected(old_motion_state, new_motion_state, state_duration)

