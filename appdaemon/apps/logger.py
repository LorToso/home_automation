import appdaemon.plugins.hass.hassapi as hass


class Logger(hass.Hass):
    def initialize(self):
        self.log('self.listen_event(self.on_event, "deconz_event")')
        self.listen_event(self.on_event, "deconz_event")

        self.log('self.listen_state(self.on_state_motion, entity="binary_sensor")')
        self.listen_state(self.on_state, entity="binary_sensor")
        self.listen_state(self.on_state, entity="light")

    def on_event(self, event_name, data, kwargs):
        self.log("--------------------------------")
        self.log("------------on_event------------")
        self.log(f"event_name: {event_name}")
        self.log(f"data: {data}")
        self.log(f"kwargs: {kwargs}")
        self.log("--------------------------------")

    def on_state(self, entity, attribute, old, new, kwargs):
        self.log("--------------------------------")
        self.log("------------on_state------------")
        self.log(f"entity: {entity}")
        self.log(f"attribute: {attribute}")
        self.log(f"old: {old}")
        self.log(f"new: {new}")
        self.log(f"kwargs: {kwargs}")
        self.log("--------------------------------")
