from base.helpers.helpers import safe_get_app
from base.input_boolean.input_boolean import InputBoolean
from base.lamps.hue_lamp import HueLamp
from base.switches.PhilipsHueSwitch import PhilipsHueSwitch
from bed_room_night_lamp import BedRoomNightLamp


class BedRoomNightSwitch(PhilipsHueSwitch):

    bed_room_head_light: HueLamp = None
    bed_room_night_light: BedRoomNightLamp = None
    night_mode: InputBoolean

    def initialize(self) -> None:
        self.switch_device_id = self.args["switch_device_id"]
        self.bed_room_head_light = safe_get_app(self, self.args["head_lamp"])
        self.bed_room_night_light = safe_get_app(self, self.args["night_lamp"])
        self.night_mode = safe_get_app(self, self.args["night_mode"])
        super().initialize()

    def on_on_clicked(self):
        self.bed_room_night_light.turn_on()

    def on_dimm_up_clicked(self):
        self.bed_room_night_light.set_color("warm_white")

    def on_dimm_down_clicked(self):
        self.bed_room_night_light.set_color("red")

    def on_off_clicked(self):
        self.bed_room_night_light.turn_off()

    def on_on_hold(self):
        self.bed_room_night_light.turn_on()
        self.bed_room_head_light.turn_on()
        self.night_mode.set_state(False)
        self.bed_room_night_light.turn_off()
        self.bed_room_night_light.turn_on()

    def on_off_hold(self):
        self.bed_room_night_light.turn_off()
        self.bed_room_head_light.turn_off()
        self.night_mode.set_state(True)
        self.bed_room_night_light.turn_on()
        self.bed_room_night_light.turn_off()
