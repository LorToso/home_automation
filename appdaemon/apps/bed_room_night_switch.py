from NightStandLamp import NightStandLamp
from base.lamps.LampFactory import LampFactory
from config import constants
from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS, MIN_BRIGHTNESS
from base.switches.PhilipsHueSwitch import PhilipsHueSwitch
from guest_mode_notification import GuestModeNotification


class BedRoomNightSwitch(PhilipsHueSwitch):

    switch_device_id: str = constants.bed_room_night_switch_id
    bed_room_head_light: HueLamp = None
    bed_room_night_light: NightStandLamp = None

    def initialize(self) -> None:
        super().initialize()
        self.bed_room_head_light = LampFactory.build_lamp(self, constants.bed_room_head_lamp_id)
        self.bed_room_night_light = LampFactory.build_lamp(self, constants.bed_room_night_lamp_id)
        self.log(f"{type(self)} initialised")

    def on_on_clicked(self):
        self.bed_room_night_light.turn_on()

    def on_dimm_up_clicked(self):
        self.bed_room_night_light.set_color("warm_white")

    def on_dimm_down_clicked(self):
        self.bed_room_night_light.set_color("red")
        #self.bed_room_night_light.reduce_brightness()
        #GuestModeNotification.send(self)

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

