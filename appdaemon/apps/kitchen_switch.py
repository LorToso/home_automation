from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS
from base.lamps.LampFactory import LampFactory
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch
import constants
from base.tts.TTS import TTS


class KitchenSwitch(IkeaTradfriSwitch):

    switch_device_id: str = constants.kitchen_switch_id
    controlled_lamp: HueLamp = None

    def initialize(self) -> None:
        super().initialize()
        self.controlled_lamp = LampFactory.build_lamp(self, constants.kitchen_lamp_id)
        self.log(f"{type(self)} initialised")

    def on_dimm_up_clicked(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.increase_brightness()

    def on_dimm_down_clicked(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.reduce_brightness()

    def on_dimm_up_hold(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.set_brightness(MAX_BRIGHTNESS)

    def on_dimm_down_hold(self):
        if self.controlled_lamp.is_on():
            self.controlled_lamp.set_brightness(20)

    def on_mid_clicked(self):
        self.controlled_lamp.toggle()

    def on_left_clicked(self):
        pass

    def on_right_clicked(self):
        TTS(self).say(
            constants.kitchen_speaker,
            "Hallo Lorenzo"
        )

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
