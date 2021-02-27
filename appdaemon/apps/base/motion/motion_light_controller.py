import appdaemon.plugins.hass.hassapi as hass

from base.helpers.helpers import it_is_dark, safe_get_app
from base.lamps.hue_lamp import HueLamp
from base.motion.aqara_motion_senor import AqaraMotionSensor


class MotionLightController(hass.Hass):

    motion_sensor: AqaraMotionSensor
    lamp: HueLamp
    turn_off_after_seconds: int
    ignore_brightness: bool

    # TODO We need some kind of light multiplexing here
    #  Should have multiple lights and maybe time dependencies?

    def initialize(self) -> None:
        self.motion_sensor = AqaraMotionSensor(
            self.args["motion_entity_id"],
            self,
            self.on_motion_detected,
            self.args["activation_boolean"]
        )
        self.lamp: HueLamp = safe_get_app(self, self.args["lamp"])

        self.turn_off_after_seconds: int = self.args['turn_light_off_after_seconds']
        self.ignore_brightness: bool = self.args["ignore_brightness"] == "true"

        self.motion_sensor.listen_to(0)
        self.motion_sensor.listen_to(self.turn_off_after_seconds)

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        if not self.ignore_brightness and not it_is_dark(self):
            self.log(f"It is not dark")
            return

        if old_motion_state == 'off' and new_motion_state == 'on' and state_duration == 0:
            self.turn_lamp_on()

        if old_motion_state == 'on' and new_motion_state == 'off' and state_duration == self.turn_off_after_seconds:
            self.turn_lamp_off()

    def turn_lamp_on(self) -> None:
        if not self.lamp.is_on():
            self.lamp.turn_on()

    def turn_lamp_off(self) -> None:
        if self.lamp.is_on():
            self.lamp.turn_off()

