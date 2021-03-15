from helpers import safe_get_app
from input_boolean import InputBoolean
from hue_lamp import HueLamp
from ikea_tradfri_switch import IkeaTradfriSwitch


class LivingRoomSwitch(IkeaTradfriSwitch):

    retro_lamp: HueLamp = None
    corner_lamp: HueLamp = None
    motion_sensor_activation: InputBoolean

    def initialize(self) -> None:
        self.retro_lamp = safe_get_app(self, self.args["retro_lamp"])
        self.corner_lamp = safe_get_app(self, self.args["corner_lamp"])
        self.motion_sensor_activation = safe_get_app(self, self.args["motion_sensor_activation"])
        super().initialize()

    def on_left_clicked(self):
        self.retro_lamp.toggle()

    def on_right_clicked(self):
        self.corner_lamp.toggle()

    def on_dimm_up_clicked(self):
        self.log("ON_DIMM_UP_CLICKED")

        if self.retro_lamp.is_on():
            self.retro_lamp.increase_brightness()
        if self.corner_lamp.is_on():
            self.corner_lamp.increase_brightness()

    def on_dimm_down_clicked(self):
        self.log("ON_DIMM_DOWN_CLICKED")

        if self.retro_lamp.is_on():
            self.retro_lamp.reduce_brightness()
        if self.corner_lamp.is_on():
            self.corner_lamp.reduce_brightness()

    def on_dimm_up_hold(self):
        self.log("ON_DIMM_UP_HOLD")
        if self.retro_lamp.is_on():
            self.retro_lamp.dimm_to_default_max()
        if self.corner_lamp.is_on():
            self.corner_lamp.dimm_to_default_max()

    def on_dimm_down_hold(self):
        self.log("ON_DIMM_DOWN_HOLD")
        if self.retro_lamp.is_on():
            self.retro_lamp.dimm_to_default_min()
        if self.corner_lamp.is_on():
            self.corner_lamp.dimm_to_default_min()

    def on_mid_clicked(self):
        if not self.retro_lamp.is_on():
            self.retro_lamp.turn_on()

        elif self.retro_lamp.is_on() and not self.corner_lamp.is_on():
            self.corner_lamp.turn_on()

        elif self.retro_lamp.is_on() and self.corner_lamp.is_on():
            self.retro_lamp.turn_off()
            self.corner_lamp.turn_off()

    def on_mid_hold(self):
        self.motion_sensor_activation.toggle()
