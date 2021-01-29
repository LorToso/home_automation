from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS
from base.motion.AqaraMotionSensor import AqaraMotionSensor
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch
import constants


class LivingRoomMotionSensor(AqaraMotionSensor):

    sensor_entity_id: str = constants.living_room_motion_sensor_id
    duration = 60
    kitchen_lamp: HueLamp = None

    def initialize(self) -> None:
        super().initialize()
        self.kitchen_lamp = HueLamp(self, constants.kitchen_lamp_id)
        self.log(f"{type(self)} initialised")

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):

        self.log(
            f"on_motion_detected. old_motion_state: {old_motion_state}, new_motion_state: {new_motion_state}, state_duration: {state_duration}")

        if old_motion_state == "off" and new_motion_state == 'on' and not self.kitchen_lamp.is_on():
            self.log(f"turning on {self.kitchen_lamp}")
            self.kitchen_lamp.turn_on()

        #and state_duration == self.duration
        if old_motion_state == "on" and new_motion_state == "off" and self.kitchen_lamp.is_on():
            self.log(f"turning off {self.kitchen_lamp}")
            self.kitchen_lamp.turn_off()

