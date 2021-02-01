import appdaemon.plugins.hass.hassapi as hass


class InputBoolean(hass.Hass):

    state: str = 'off'
    entity_id: str = "no_id"

    def initialize(self) -> None:
        self.entity_id = self.args["entity_id"]
        self.listen_state(self.on_state_change, entity=self.entity_id, immediate=True)

    def toggle(self, **kwargs) -> None:
        super().toggle(self.entity_id, **kwargs)

    def set_state(self, state: bool, **kwargs) -> None:
        if state:
            super().set_state(self.entity_id, state='on')
        else:
            super().set_state(self.entity_id, state='off')

    def on_state_change(self, entity, attribute, old, new, kwargs) -> None:
        self.state = new
        self.log(f"State of entity {entity} is now {new}")
        self.on_state(old, new)

    def on_state(self, old_state: str, new_state: str):
        pass

    def is_on(self) -> bool:
        return self.state == 'on'

    def is_off(self) -> bool:
        return self.state == 'off'
