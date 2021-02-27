import appdaemon.plugins.hass.hassapi as hass


class Logger(hass.Hass):
    def initialize(self):
        self.log('self.listen_event(self.on_event, "deconz_event")')
        self.listen_event(self.on_event, "deconz_event")

        self.log('self.listen_state(self.on_state_motion, entity="binary_sensor")')
        self.listen_state(self.on_state, entity="binary_sensor")
        self.listen_state(self.on_state, entity="light")
        self.listen_state(self.on_state, entity="light", attribute='brightness')
        self.listen_state(self.on_state, entity="input_boolean")
        self.listen_event(self.on_event, "mobile_app_notification_action")
        self.listen_state(self.on_state, entity="media_player")

    def on_event(self, event_name, data, kwargs):
        self.log(f"--on_event: event_name: {event_name}, data: {data}, kwargs: {kwargs}")

    def on_state(self, entity, attribute, old, new, kwargs):
        self.log(f"--on_state: entity: {entity}, attribute: {attribute}, old: {old}, new: {new}, kwargs: {kwargs}")
