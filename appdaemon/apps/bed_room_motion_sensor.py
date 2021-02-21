from base.information.information import it_is_dark
from base.input_boolean.input_boolean import InputBoolean
from base.lamps.hue_lamp import HueLamp
from base.motion.AqaraMotionSensor import AqaraMotionSensor
from base.motion.MusicFollowingController import MusicFollowingController


class BedRoomMotionSensor(AqaraMotionSensor):
    activation_boolean: InputBoolean
    music_following_controller: MusicFollowingController
    head_lamp: HueLamp
    night_lamp: HueLamp
    night_mode: InputBoolean
    turn_light_off_after_seconds: int

    def initialize(self) -> None:
        super().initialize()
        self.activation_boolean = self.get_app(self.args["activation_boolean"])
        self.head_lamp = self.get_app(self.args["head_lamp"])
        self.night_lamp = self.get_app(self.args["night_lamp"])
        self.turn_light_off_after_seconds = self.args['turn_light_off_after_seconds']
        self.night_mode = self.get_app(self.args["night_mode"])
        self.music_following_controller = MusicFollowingController(self)

        self.listen_to(0)
        self.listen_to(self.turn_light_off_after_seconds)

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        if self.activation_boolean.is_off() and self.night_mode.is_off():
            self.log(f"Skipping action. "
                     f"activation_boolean: {self.activation_boolean.state}, "
                     f"night_mode: {self.night_mode.state}")
            return

        self.music_following_controller.on_motion_detected(old_motion_state, new_motion_state, state_duration)

        if old_motion_state == 'off' and new_motion_state == 'on' and state_duration == 0:
            if it_is_dark(self) and not self.night_lamp.is_on():
                self.head_lamp.turn_on()

        if old_motion_state == 'on' and new_motion_state == 'off' and state_duration == self.turn_light_off_after_seconds:
            self.head_lamp.turn_off()

