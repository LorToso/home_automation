from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch
import constants


class BadRoomSwitch(IkeaTradfriSwitch):

    switch_device_id: str = constants.bed_room_head_lamp_id
    bed_room_head_light: HueLamp = None
    bed_room_night_light: HueLamp = None

    def initialize(self) -> None:
        super().initialize()
        self.bed_room_head_light = HueLamp(self, constants.bed_room_head_lamp_id)
        self.bed_room_night_light = HueLamp(self, constants.bed_room_night_lamp_id)
        self.log(f"{type(self)} initialised")

    def on_left_clicked(self):
        pass

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
            self.bed_room_head_light.set_brightness(MAX_BRIGHTNESS)

    def on_dimm_down_hold(self):
        if self.bed_room_head_light.is_on():
            self.bed_room_head_light.set_brightness(20)

    def on_mid_clicked(self):
        self.bed_room_head_light.toggle()

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
