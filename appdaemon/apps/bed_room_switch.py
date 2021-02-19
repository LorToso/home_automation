from base.lamps.hue_lamp import HueLamp
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch
from bed_room_night_lamp import BedRoomNightLamp


class BedRoomSwitch(IkeaTradfriSwitch):

    bed_room_head_light: HueLamp = None
    bed_room_night_light: BedRoomNightLamp = None

    def initialize(self) -> None:
        self.switch_device_id = self.args["switch_device_id"]
        self.bed_room_head_light = self.get_app(self.args["head_lamp"])
        self.bed_room_night_light = self.get_app(self.args["night_lamp"])
        super().initialize()
        self.log(f"{type(self)} initialised")

    def on_mid_clicked(self):
        self.bed_room_head_light.toggle()

    def on_right_clicked(self):
        self.bed_room_night_light.toggle()

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