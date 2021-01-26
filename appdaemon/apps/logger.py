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


class Logger(hass.Hass):
    id = 'wohnzimmer_schalter'
    device_id = 'e70207e80c0b11ebaf5719ccebfd3949'

    def initialize(self):
        self.listen_event(self.on_event, "deconz_event")

    def on_event(self, event_name, data, kwargs):
        self.log("--------------------------------")
        self.log(f"event_name: {event_name}")
        self.log(f"data: {data}")
        self.log(f"kwargs: {kwargs}")
        self.log("--------------------------------")



