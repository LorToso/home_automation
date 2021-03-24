from helpers import safe_get_app
from input_boolean import InputBoolean
from hue_lamp import HueLamp
from lamp_multiplexer_app import LampMultiplexerApp
from ikea_tradfri_switch import IkeaTradfriSwitch


class LivingRoomSwitch(IkeaTradfriSwitch):

    retro_lamp: HueLamp = None
    corner_lamp: HueLamp = None
    head_lamp: LampMultiplexerApp = None
    motion_sensor_activation: InputBoolean

    def initialize(self) -> None:
        self.head_lamp = safe_get_app(self, self.args["head_lamp"])
        self.retro_lamp = safe_get_app(self, self.args["retro_lamp"])
        self.corner_lamp = safe_get_app(self, self.args["corner_lamp"])

        self.motion_sensor_activation = safe_get_app(self, self.args["motion_sensor_activation"])
        super().initialize()

    def on_left_clicked(self):
        self.retro_lamp.toggle()

    def on_right_clicked(self):
        self.corner_lamp.toggle()

    def on_mid_clicked(self):
        self.head_lamp.toggle()

    def on_dimm_up_clicked(self):
        if self.retro_lamp.is_on():
            self.retro_lamp.increase_brightness()
        if self.corner_lamp.is_on():
            self.corner_lamp.increase_brightness()
        if self.head_lamp.is_on():
            self.head_lamp.increase_brightness()

    def on_dimm_down_clicked(self):
        if self.retro_lamp.is_on():
            self.retro_lamp.reduce_brightness()
        if self.corner_lamp.is_on():
            self.corner_lamp.reduce_brightness()
        if self.head_lamp.is_on():
            self.head_lamp.reduce_brightness()

    def on_dimm_up_hold(self):
        if self.retro_lamp.is_on():
            self.retro_lamp.dimm_to_default_max()
        if self.corner_lamp.is_on():
            self.corner_lamp.dimm_to_default_max()
        if self.head_lamp.is_on():
            self.head_lamp.dimm_to_default_max()

    def on_dimm_down_hold(self):
        if self.retro_lamp.is_on():
            self.retro_lamp.dimm_to_default_min()
        if self.corner_lamp.is_on():
            self.corner_lamp.dimm_to_default_min()
        if self.head_lamp.is_on():
            self.head_lamp.dimm_to_default_min()

    def on_mid_hold(self):
        self.motion_sensor_activation.toggle()
