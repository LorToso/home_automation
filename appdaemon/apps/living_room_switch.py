from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch
import constants
from base.tts.TTS import TTS


class LivingRoomSwitch(IkeaTradfriSwitch):

    switch_device_id: str = constants.living_room_switch_id
    retro_lamp: HueLamp = None
    corner_lamp: HueLamp = None

    def initialize(self) -> None:
        super().initialize()
        self.retro_lamp = HueLamp(self, constants.living_room_retro_lamp_id)
        self.corner_lamp = HueLamp(self, constants.living_room_corner_lamp_id)
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

    TTS(self).broad_cast(
        # service="tts/google_say",
        # entity_id=constants.bath_room_speaker,
        message='Das ist ein test.',
        language="de"
    )
    pass

    def on_dimm_down_clicked(self):

        if self.retro_lamp.is_on():
            self.retro_lamp.reduce_brightness()
        if self.corner_lamp.is_on():
            self.corner_lamp.reduce_brightness()

    def on_dimm_up_hold(self):
        if self.retro_lamp.is_on():
            self.retro_lamp.set_brightness(MAX_BRIGHTNESS)
        if self.corner_lamp.is_on():
            self.corner_lamp.set_brightness(MAX_BRIGHTNESS)

    def on_dimm_down_hold(self):
        if self.retro_lamp.is_on():
            self.retro_lamp.set_brightness(20)
        if self.corner_lamp.is_on():
            self.corner_lamp.set_brightness(20)

    def on_mid_clicked(self):
        if not self.retro_lamp.is_on():
            self.retro_lamp.turn_on()

        elif self.retro_lamp.is_on() and not self.corner_lamp.is_on():
            self.corner_lamp.turn_on()

        elif self.retro_lamp.is_on() and self.corner_lamp.is_on():
            self.retro_lamp.turn_off()
            self.corner_lamp.turn_off()

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
