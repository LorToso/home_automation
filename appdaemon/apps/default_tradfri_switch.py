from base.lamps.HueLamp import HueLamp, MAX_BRIGHTNESS
from base.lamps.LampFactory import LampFactory
from base.switches.IkeaTradfriSwitch import IkeaTradfriSwitch
import constants


class DefaultTradfriSwitch(IkeaTradfriSwitch):

    controlled_lamp: HueLamp = None

    def initialize(self) -> None:
        self.switch_device_id = self.args['switch_device_id']
        self.controlled_lamp = LampFactory.build_lamp(self, self.args['lamp_entity_id'])
        
        super().initialize()

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
        pass

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
