import appdaemon.plugins.hass.hassapi as hass

# Nachttisch Schalter
# 'device_id': 'aba7647ac6470849cea271f62559e2db'
# events:
#   on
#   dimm up pressed 2000
#   dimm up hold 2002
#   dimm up release 2003


buttons = {'MID': 1, 'UP': 2, 'DOWN': 3, 'LEFT': 4, 'RIGHT': 5}
releases = {'HOLD': 1, 'CLICK': 2, 'RELEASE': 3}


class HelloWorld(hass.Hass):
    id = 'wohnzimmer_schalter'
    unique_id = '58:8e:81:ff:fe:56:d9:8a'
    device_id = 'e70207e80c0b11ebaf5719ccebfd3949'

    def initialize(self):
        self.log("Hello from AppDaemon")
        self.log("You are now ready to run Apps!")
        self.log('listening to "deconz_event"')
        self.listen_event(self.click, "deconz_event")

    def click(self, event_name, data, kwargs):
        self.log(f"event_name: {event_name}")
        self.log(f"data: {data}")
        self.log(f"kwargs: {kwargs}")

        #state = self.get_state("light.office_1", attribute="all")
        state = self.get_state('light.kitchen_lamp', attribute="all")
        self.log(f"{state}")


        #if data["device_id"] != self.device_id:
        #    pass

        if data['event'] == self.get_code("RIGHT", "CLICK"):
            self.log("RIGHT GEKLICKT")
            self.turn_on('light.kitchen_lamp', brightness=50)
            #self.set_state('light.kitchen_lamp', state="on")


        pass

    def get_code(self, button, release):
        return int(f"{buttons[button]}00{releases[release]}")
