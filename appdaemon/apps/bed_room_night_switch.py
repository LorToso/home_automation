import constants
from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS, MIN_BRIGHTNESS
from base.switches.PhilipsHueSwitch import PhilipsHueSwitch


class BedRoomNightSwitch(PhilipsHueSwitch):

    switch_device_id: str = constants.bed_room_night_switch_id
    bed_room_head_light: HueLamp = None
    bed_room_night_light: HueLamp = None

    def initialize(self) -> None:
        super().initialize()
        self.bed_room_head_light = HueLamp(self, constants.bed_room_head_lamp_id)
        self.bed_room_night_light = HueLamp(self, constants.bed_room_night_lamp_id)
        self.log(f"{type(self)} initialised")

    def on_on_clicked(self):
        self.bed_room_night_light.turn_on()

    def on_dimm_up_clicked(self):
        self.bed_room_night_light.increase_brightness()

    def on_dimm_down_clicked(self):
        self.bed_room_night_light.reduce_brightness()

    def on_off_clicked(self):
        self.bed_room_night_light.turn_off()

    def on_on_hold(self):
        self.bed_room_night_light.turn_on()
        self.bed_room_head_light.turn_on()

    def on_dimm_up_hold(self):
        self.bed_room_night_light.set_brightness(MAX_BRIGHTNESS)

        if self.bed_room_head_light.is_on():
            self.bed_room_head_light.set_brightness(MAX_BRIGHTNESS)

    def on_dimm_down_hold(self):
        self.bed_room_night_light.set_brightness(MIN_BRIGHTNESS)
        if self.bed_room_head_light.is_on():
            self.bed_room_head_light.set_brightness(MIN_BRIGHTNESS)

    def on_off_hold(self):
        self.bed_room_night_light.turn_off()
        self.bed_room_head_light.turn_off()

    def on_on_released(self):
        pass

    def on_dimm_up_released(self):
        pass

    def on_dimm_down_released(self):
        pass

    def on_off_released(self):
        pass
