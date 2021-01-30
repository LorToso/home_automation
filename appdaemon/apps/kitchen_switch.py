from typing import Optional

from base.input_boolean.input_boolean import InputBoolean
from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS
from base.lamps.LampFactory import LampFactory
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch
import constants
from base.tts.TTS import TTS


class KitchenSwitch(IkeaTradfriSwitch):

    switch_device_id: str = constants.kitchen_switch_id
    controlled_lamp: HueLamp = None
    motion_sensor_activation_boolean: Optional[InputBoolean]

    def initialize(self) -> None:
        super().initialize()
        self.controlled_lamp = LampFactory.build_lamp(self, constants.kitchen_lamp_id)
        self.motion_sensor_activation_boolean = InputBoolean(self, constants.kitchen_motion_activation_boolean)
        self.log(f"{type(self)} initialised")

    def on_dimm_up_clicked(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.increase_brightness()

    def on_dimm_down_clicked(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.reduce_brightness()

    def on_dimm_up_hold(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.set_brightness(MAX_BRIGHTNESS)

    def on_dimm_down_hold(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.set_brightness(20)

    def on_mid_clicked(self):
        self.controlled_lamp.toggle()

    def on_left_clicked(self):
        if self.motion_sensor_activation_boolean.is_on():
            self.log(f"Turning off motion sensor [{constants.kitchen_motion_sensor_id}]")
        if self.motion_sensor_activation_boolean.is_off():
            self.log(f"Turning on motion sensor [{constants.kitchen_motion_sensor_id}]")

        self.motion_sensor_activation_boolean.toggle()

    def on_right_clicked(self):
        TTS(self).say(
            constants.kitchen_speaker,
            "Hallo Lorenzo"
        )

    def on_mid_hold(self):
        pass

    def on_left_hold(self):
        pass

    def on_right_hold(self):
        pass

    def on_dimm_down_release(self):
        pass

    def on_dimm_up_release(self):
        pass

    def on_left_release(self):
        pass

    def on_right_release(self):
        pass

    def on_mid_release(self):
        pass
