from typing import Optional

from base.input_boolean.input_boolean import InputBoolean
from base.lamps.HueLamp import HueLamp
from base.lamps.LampFactory import LampFactory
from base.motion.AqaraMotionSensor import AqaraMotionSensor


class LightControllingMotionSensor(AqaraMotionSensor):

    lamp: HueLamp = None
    turn_off_after_seconds: int = 0
    activation_boolean: Optional[InputBoolean]

    def initialize(self) -> None:
        self.motion_entity_id = self.args['motion_entity_id']
        self.lamp = LampFactory.build_lamp(self, self.args['lamp_entity_id'])
        self.turn_off_after_seconds = self.args['turn_off_after_seconds']

        if 'activation_boolean' in self.args:
            self.activation_boolean = InputBoolean(self, self.args['activation_boolean'])
        else:
            self.activation_boolean = None

        self.durations = [0, self.turn_off_after_seconds]
        super().initialize()

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        if self.activation_boolean is not None and self.activation_boolean.is_off():
            self.log(f"Skipping action. {self.activation_boolean.entity_id} is in state {self.activation_boolean.state}")
            pass

        if old_motion_state == "off" and new_motion_state == 'on' and not self.lamp.is_on() and state_duration == 0:
            self.log(f"turning on {self.lamp.entity_id}")
            self.lamp.turn_on()

        if old_motion_state == "on" and new_motion_state == "off" and self.lamp.is_on() and state_duration == self.turn_off_after_seconds:
            self.log(f"turning off {self.lamp.entity_id}")
            self.lamp.turn_off()

