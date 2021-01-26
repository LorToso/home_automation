from abc import abstractmethod
from typing import Any, Dict

import appdaemon.plugins.hass.hassapi as hass

# Nachttisch Schalter
# 'device_id': 'aba7647ac6470849cea271f62559e2db'
from appdaemon.appdaemon import AppDaemon

buttons = {'MID': 1, 'UP': 2, 'DOWN': 3, 'LEFT': 4, 'RIGHT': 5}
releases = {'HOLD': 1, 'CLICK': 2, 'RELEASE': 3}


class IkeaTradfriSwitch(hass.Hass):

    switch_device_id: str = "0"

    def initialize(self) -> None:
        self.log(f'listening to "deconz_event" for id {self.switch_device_id}')
        self.listen_event(self.click, "deconz_event", device_id=self.switch_device_id)

    def click(self, event_name: str, data: Dict[str, Any], kwargs: Dict[str, Any]) -> None:
        self.log(f"Received event {data}")

        if data['event'] == self.get_code("LEFT", "CLICK"):
            self.log("on_left_clicked")
            self.on_left_clicked()
        elif data['event'] == self.get_code("RIGHT", "CLICK"):
            self.log("on_right_clicked")
            self.on_right_clicked()
        elif data['event'] == self.get_code("UP", "CLICK"):
            self.log("on_dimm_up_clicked")
            self.on_dimm_up_clicked()
        elif data['event'] == self.get_code("DOWN", "CLICK"):
            self.log("on_dimm_up_clicked")
            self.on_dimm_down_clicked()
        elif data['event'] == self.get_code("MID", "CLICK"):
            self.log("on_mid_clicked")
            self.on_mid_clicked()

        elif data['event'] == self.get_code("LEFT", "HOLD"):
            self.log("on_left_hold")
            self.on_left_hold()
        elif data['event'] == self.get_code("RIGHT", "HOLD"):
            self.log("on_right_hold")
            self.on_right_hold()
        elif data['event'] == self.get_code("UP", "HOLD"):
            self.log("on_dimm_up_hold")
            self.on_dimm_up_hold()
        elif data['event'] == self.get_code("DOWN", "HOLD"):
            self.log("on_dimm_down_hold")
            self.on_dimm_down_hold()
        elif data['event'] == self.get_code("MID", "HOLD"):
            self.log("on_mid_hold")
            self.on_mid_hold()

        elif data['event'] == self.get_code("LEFT", "RELEASE"):
            self.log("on_left_release")
            self.on_left_release()
        elif data['event'] == self.get_code("RIGHT", "RELEASE"):
            self.log("on_right_release")
            self.on_right_release()
        elif data['event'] == self.get_code("UP", "RELEASE"):
            self.log("on_dimm_up_release")
            self.on_dimm_up_release()
        elif data['event'] == self.get_code("DOWN", "RELEASE"):
            self.log("on_dimm_down_release")
            self.on_dimm_down_release()
        elif data['event'] == self.get_code("MID", "RELEASE"):
            self.log("on_mid_release")
            self.on_mid_release()

    def get_code(self, button: str, release: str) -> int:
        return int(f"{buttons[button]}00{releases[release]}")

    @abstractmethod
    def on_left_clicked(self):
        pass

    @abstractmethod
    def on_right_clicked(self):
        pass

    @abstractmethod
    def on_dimm_up_clicked(self):
        pass

    @abstractmethod
    def on_dimm_down_clicked(self):
        pass

    @abstractmethod
    def on_mid_clicked(self):
        pass

    @abstractmethod
    def on_left_hold(self):
        pass

    @abstractmethod
    def on_right_hold(self):
        pass

    @abstractmethod
    def on_dimm_up_hold(self):
        pass

    @abstractmethod
    def on_dimm_down_hold(self):
        pass

    @abstractmethod
    def on_mid_hold(self):
        pass

    @abstractmethod
    def on_dimm_down_release(self):
        pass

    @abstractmethod
    def on_dimm_up_release(self):
        pass

    @abstractmethod
    def on_left_release(self):
        pass

    @abstractmethod
    def on_right_release(self):
        pass

    @abstractmethod
    def on_mid_release(self):
        pass
