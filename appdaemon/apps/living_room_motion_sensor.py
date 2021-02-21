from typing import Optional

from base.information.information import it_is_dark
from base.input_boolean.input_boolean import InputBoolean
from base.lamps.hue_lamp import HueLamp
from base.motion.AqaraMotionSensor import AqaraMotionSensor
from base.motion.MusicFollowingController import MusicFollowingController


class LivingRoomMotionSensor(AqaraMotionSensor):
    activation_boolean: InputBoolean
    music_following_controller: MusicFollowingController
    corner_lamp: HueLamp
    retro_lamp: HueLamp
    turn_light_off_after_seconds: int

    def initialize(self) -> None:
        super().initialize()
        self.activation_boolean = self.get_app(self.args["activation_boolean"])
        self.retro_lamp = self.get_app(self.args["retro_lamp"])
        self.corner_lamp = self.get_app(self.args["corner_lamp"])
        self.turn_light_off_after_seconds = self.args['turn_light_off_after_seconds']
        self.music_following_controller = MusicFollowingController(self)

        self.listen_to(0)
        self.listen_to(self.turn_light_off_after_seconds)

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        if self.activation_boolean.is_off():
            self.log(f"Skipping action. {self.activation_boolean.entity_id} is in state {self.activation_boolean.state}")
            return

        self.music_following_controller.on_motion_detected(old_motion_state, new_motion_state, state_duration)

        if old_motion_state == 'off' and new_motion_state == 'on' and state_duration == 0:
            if it_is_dark(self) and self.retro_lamp.is_off() and self.corner_lamp.is_off():
                self.retro_lamp.turn_on()
                self.corner_lamp.turn_on()

        if old_motion_state == 'on' and new_motion_state == 'off' and state_duration == self.turn_light_off_after_seconds:
            if not self.music_following_controller.speaker.is_playing():
                self.retro_lamp.turn_off()
                self.corner_lamp.turn_off()

