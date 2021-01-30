from typing import Optional

from base.input_boolean.input_boolean import InputBoolean
from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS
from base.lamps.LampFactory import LampFactory
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch


class DefaultTradfriSwitch(IkeaTradfriSwitch):

    controlled_lamp: HueLamp = None
    default_dimmed_brightness: int = 50
    motion_sensor_activation_boolean: Optional[InputBoolean] = None

    def initialize(self) -> None:
        self.switch_device_id = self.args['switch_device_id']
        self.controlled_lamp = LampFactory.build_lamp(self, self.args['lamp_entity_id'])
        self.default_dimmed_brightness = self.args['default_dimmed_brightness']

        if 'motion_activation_boolean' in self.args:
            self.motion_sensor_activation_boolean = InputBoolean(self, self.args['motion_activation_boolean'])

        super().initialize()

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
            self.controlled_lamp.set_brightness(self.default_dimmed_brightness)

    def on_mid_clicked(self):
        self.controlled_lamp.toggle()

    def on_left_clicked(self):
        self.motion_sensor_activation_boolean.toggle()
