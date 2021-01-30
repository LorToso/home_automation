from base.lamps.HueLamp import HueLamp
from base.switches.PhilipsHueSwitch import PhilipsHueSwitch
from bed_room_night_lamp import BedRoomNightLamp


class BedRoomNightSwitch(PhilipsHueSwitch):

    bed_room_head_light: HueLamp = None
    bed_room_night_light: BedRoomNightLamp = None

    def initialize(self) -> None:
        self.switch_device_id = self.args["switch_device_id"]
        self.bed_room_head_light = self.get_app(self.args["head_lamp_app_name"])
        self.bed_room_night_light = self.get_app(self.args["night_lamp_app_name"])
        super().initialize()
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

    def on_off_hold(self):
        self.bed_room_night_light.turn_off()
        self.bed_room_head_light.turn_off()

