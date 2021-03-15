from helpers import safe_get_app
from input_boolean import InputBoolean
from hue_lamp import HueLamp
from ikea_tradfri_switch import IkeaTradfriSwitch
from bed_room_night_lamp import BedRoomNightLamp


class BedRoomSwitch(IkeaTradfriSwitch):

    bed_room_head_light: HueLamp = None
    bed_room_night_light: BedRoomNightLamp = None
    motion_sensor_activation_boolean: InputBoolean = None

    def initialize(self) -> None:
        self.switch_device_id = self.args["switch_device_id"]
        self.bed_room_head_light = safe_get_app(self, self.args["head_lamp"])
        self.bed_room_night_light = safe_get_app(self, self.args["night_lamp"])
        self.motion_sensor_activation_boolean = safe_get_app(self, self.args["motion_activation_boolean"])

        super().initialize()

    def on_mid_clicked(self):
        self.log("XXX ON MID CLICKED")
        self.bed_room_head_light.toggle()

    def on_right_clicked(self):
        self.log("XXX ON RIGHT CLICKED")
        self.bed_room_night_light.toggle()

    def on_mid_hold(self):
        self.log("XXX ON MID HOLD")
        self.bed_room_night_light.toggle_scene()

    def on_mid_release(self):
        self.log("XXX ON MID RELEASE")

    def on_left_clicked(self):
        self.motion_sensor_activation_boolean.toggle()

    def on_dimm_up_clicked(self):
        if self.bed_room_head_light.is_on():
            self.bed_room_head_light.increase_brightness()

    def on_dimm_down_clicked(self):
        if self.bed_room_head_light.is_on():
            self.bed_room_head_light.reduce_brightness()

    def on_dimm_up_hold(self):
        if self.bed_room_head_light.is_on():
            self.bed_room_head_light.dimm_to_default_max()

    def on_dimm_down_hold(self):
        if self.bed_room_head_light.is_on():
            self.bed_room_head_light.dimm_to_default_min()
