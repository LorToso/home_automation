from base.lamps.HueLamp import HueLamp
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch


class LivingRoomSwitch(IkeaTradfriSwitch):

    retro_lamp: HueLamp = None
    corner_lamp: HueLamp = None

    def initialize(self) -> None:
        self.switch_device_id = self.args["switch_device_id"]
        self.retro_lamp = self.get_app(self.args["retro_lamp_app_name"])
        self.corner_lamp = self.get_app(self.args["corner_lamp_app_name"])
        super().initialize()
        self.log(f"{type(self)} initialised")

    def on_left_clicked(self):
        self.retro_lamp.toggle()

    def on_right_clicked(self):
        self.corner_lamp.toggle()

    def on_dimm_up_clicked(self):

        if self.retro_lamp.is_on():
            self.retro_lamp.increase_brightness()
        if self.corner_lamp.is_on():
            self.corner_lamp.increase_brightness()

    def on_dimm_down_clicked(self):

        if self.retro_lamp.is_on():
            self.retro_lamp.reduce_brightness()
        if self.corner_lamp.is_on():
            self.corner_lamp.reduce_brightness()

    def on_dimm_up_hold(self):
        if self.retro_lamp.is_on():
            self.retro_lamp.dimm_to_default_max()
        if self.corner_lamp.is_on():
            self.corner_lamp.dimm_to_default_max()

    def on_dimm_down_hold(self):
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

