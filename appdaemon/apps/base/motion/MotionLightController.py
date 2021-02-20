from base.information.information import it_is_dark
from base.lamps.hue_lamp import HueLamp
from base.motion.AqaraMotionSensor import AqaraMotionSensor


class MotionLightController:

    def __init__(
            self,
            controller: AqaraMotionSensor,
            ignore_brightness: bool = False
    ):
        self.controller: AqaraMotionSensor = controller
        self.lamp: HueLamp = controller.get_app(controller.args["lamp"])
        self.turn_off_after_seconds: int = controller.args['turn_light_off_after_seconds']
        self.ignore_brightness = ignore_brightness

        controller.listen_to(0)
        controller.listen_to(self.turn_off_after_seconds)

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        if not self.ignore_brightness and not it_is_dark(self.controller):
            self.controller.log(f"It is not dark")
            return

        if old_motion_state == 'off' and new_motion_state == 'on' and state_duration == 0:
            self.turn_lamp_on()

        if old_motion_state == 'on' and new_motion_state == 'off' and state_duration == self.turn_off_after_seconds:
            self.turn_lamp_off()

    def turn_lamp_on(self) -> None:
        if not self.lamp.is_on():
            self.controller.log(f"turning on {self.lamp.entity_id}")
            self.lamp.turn_on()

    def turn_lamp_off(self) -> None:
        if self.lamp.is_on():
            self.controller.log(f"turning off {self.lamp.entity_id}")
            self.lamp.turn_off()

