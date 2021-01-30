import appdaemon.plugins.hass.hassapi as hass


class InputBoolean:

    state: str = 'off'

    def __init__(self, controller: hass.Hass, entity_id: str):

        self.controller = controller
        self.entity_id = entity_id

        self.controller.listen_state(self.on_state_change, entity=entity_id, immediate=True)

    def toggle(self) -> None:
        self.controller.toggle(self.entity_id)

    def set_state(self, state: bool) -> None:
        if state:
            self.controller.set_state(self.entity_id, state='on')
        else:
            self.controller.set_state(self.entity_id, state='off')

    def on_state_change(self, entity, attribute, old, new, kwargs) -> None:
        self.state = new

    def is_on(self) -> bool:
        return self.state == 'on'

    def is_off(self) -> bool:
        return self.state == 'off'
