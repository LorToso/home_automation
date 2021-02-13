from typing import Optional

from base.input_boolean.input_boolean import InputBoolean
from base.lamps.HueLamp import HueLamp
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch


class DefaultTradfriSwitch(IkeaTradfriSwitch):

    controlled_lamp: HueLamp = None
    default_dimmed_brightness: int = 50
    motion_sensor_activation_boolean: Optional[InputBoolean] = None

    def initialize(self) -> None:
        self.controlled_lamp = self.get_app(self.args["lamp_app_name"])

        if 'motion_activation_boolean_app_name' in self.args:
            self.log("initialising motion_sensor_activation_boolean")
            self.motion_sensor_activation_boolean = self.get_app(self.args["motion_activation_boolean_app_name"])

        super().initialize()

    def on_dimm_up_clicked(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.increase_brightness()

    def on_dimm_down_clicked(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.reduce_brightness()

    def on_dimm_up_hold(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.dimm_to_default_max()

    def on_dimm_down_hold(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.dimm_to_default_min()

    def on_mid_clicked(self):
        self.controlled_lamp.toggle()

    def on_left_clicked(self):
        self.log("on_left_clicked")
        if self.motion_sensor_activation_boolean is not None:
            self.log("toggling motion_sensor_activation_boolean")
            self.motion_sensor_activation_boolean.toggle()
