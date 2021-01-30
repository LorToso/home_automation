from abc import abstractmethod
from typing import Any, Dict

import appdaemon.plugins.hass.hassapi as hass

buttons = {'ON': 1, 'DIMM_UP': 2, 'DIMM_DOWN': 3, 'OFF': 4}
releases = {'CLICK': 0, 'HOLD': 1, 'RELEASE': 2}


class PhilipsHueSwitch(hass.Hass):

    switch_device_id: str = "0"

    def initialize(self) -> None:
        self.log(f'listening to "deconz_event" for id {self.switch_device_id}')
        self.listen_event(self.click, "deconz_event", device_id=self.switch_device_id)

    def click(self, event_name: str, data: Dict[str, Any], kwargs: Dict[str, Any]) -> None:
        #self.log(f"Received event {data}")

        if data['event'] == self.get_code("ON", "CLICK"):
            self.log("on_on_clicked")
            self.on_on_clicked()
        elif data['event'] == self.get_code("DIMM_UP", "CLICK"):
            self.log("on_dimm_up_clicked")
            self.on_dimm_up_clicked()
        elif data['event'] == self.get_code("DIMM_DOWN", "CLICK"):
            self.log("on_dimm_down_clicked")
            self.on_dimm_down_clicked()
        elif data['event'] == self.get_code("OFF", "CLICK"):
            self.log("on_off_clicked")
            self.on_off_clicked()

        elif data['event'] == self.get_code("ON", "RELEASE"):
            self.log("on_on_released")
            self.on_on_released()
        elif data['event'] == self.get_code("DIMM_UP", "RELEASE"):
            self.log("on_dimm_up_released")
            self.on_dimm_up_released()
        elif data['event'] == self.get_code("DIMM_DOWN", "RELEASE"):
            self.log("on_dimm_down_released")
            self.on_dimm_down_released()
        elif data['event'] == self.get_code("OFF", "RELEASE"):
            self.log("on_off_released")
            self.on_off_released()

        elif data['event'] == self.get_code("ON", "HOLD"):
            self.log("on_on_hold")
            self.on_on_hold()
        elif data['event'] == self.get_code("DIMM_UP", "HOLD"):
            self.log("on_dimm_up_hold")
            self.on_dimm_up_hold()
        elif data['event'] == self.get_code("DIMM_DOWN", "HOLD"):
            self.log("on_dimm_up_hold")
            self.on_dimm_up_hold()
        elif data['event'] == self.get_code("OFF", "HOLD"):
            self.log("on_off_hold")
            self.on_off_hold()

    @staticmethod
    def get_code(button: str, release: str) -> int:
        return int(f"{buttons[button]}00{releases[release]}")

    def on_on_clicked(self):
        pass

    def on_dimm_up_clicked(self):
        pass

    def on_dimm_down_clicked(self):
        pass

    def on_off_clicked(self):
        pass

    def on_on_hold(self):
        pass

    def on_dimm_up_hold(self):
        pass

    def on_dimm_down_hold(self):
        pass

    def on_off_hold(self):
        pass

    def on_on_released(self):
        pass

    def on_dimm_up_released(self):
        pass

    def on_dimm_down_released(self):
        pass

    def on_off_released(self):
        pass
