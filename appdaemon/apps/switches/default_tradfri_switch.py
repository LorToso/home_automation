from helpers import safe_get_app
from input_boolean import InputBoolean
from hue_lamp import HueLamp
from ikea_tradfri_switch import IkeaTradfriSwitch


class DefaultTradfriSwitch(IkeaTradfriSwitch):

    controlled_lamp: HueLamp = None
    default_dimmed_brightness: int = 50
    motion_sensor_activation_boolean: InputBoolean

    def initialize(self) -> None:
        self.controlled_lamp = safe_get_app(self, self.args["lamp"])
        self.motion_sensor_activation_boolean = safe_get_app(self, self.args["motion_activation_boolean"])

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
        self.motion_sensor_activation_boolean.toggle()
