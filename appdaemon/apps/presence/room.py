import appdaemon.plugins.hass.hassapi as hass


class Room:

    def __init__(
            self,
            controller: hass.Hass,
            motion_sensor: str,
            input_boolean: str
    ):
        self.controller = controller
        self.motion_sensor = motion_sensor
        self.presence_boolean = input_boolean

        self.state = "off"

    def is_present(self) -> bool:
        return self.state == "on"

    def set_presence(self, active: bool):
        if active:
            self.controller.turn_on(self.presence_boolean)
        else:
            self.controller.turn_off(self.presence_boolean)


