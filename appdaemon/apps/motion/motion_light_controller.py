import appdaemon.plugins.hass.hassapi as hass

from helpers import it_is_dark, safe_get_app
from lamp_like import LampLike

from boolean_set import BooleanSet


class MotionLightController(hass.Hass):
    lamp: LampLike
    boolean_set: BooleanSet
    turn_off_after_seconds: int
    ignore_brightness: bool

    def initialize(self) -> None:
        self.lamp: LampLike = self.create_lamp()
        self.boolean_set = BooleanSet(self, self.args["activation_boolean"])

        self.turn_off_after_seconds: int = self.args['turn_light_off_after_seconds']
        self.ignore_brightness: bool = self.args["ignore_brightness"]

        self.listen_to(self.args["presence_boolean"], 0)
        self.listen_to(self.args["presence_boolean"], self.turn_off_after_seconds)

    def listen_to(self, presence_boolean: str, duration: int):
        self.listen_state(
            callback=self.on_presence_changed,
            entity=presence_boolean,
            immediate=True,
            duration=duration,
            state_duration=duration,
        )

    def create_lamp(self) -> LampLike:
        return safe_get_app(self, self.args["lamp"])

    def on_presence_changed(self, entity, attribute, old_presence_state, new_presence_state, kwargs) -> None:
        if not self.boolean_set.is_active():
            self.boolean_set.log_states()
            self.log("Skipping action...")
            return

        if not self.ignore_brightness and not it_is_dark(self):
            self.log(f"It is not dark")
            return

        if old_presence_state == 'off' and new_presence_state == 'on' and kwargs['state_duration'] == 0:
            self.turn_lamp_on()

        if old_presence_state == 'on' and new_presence_state == 'off' and kwargs['state_duration'] == self.turn_off_after_seconds:
            self.turn_lamp_off()

    def turn_lamp_on(self) -> None:
        if not self.lamp.is_on():
            self.lamp.turn_on()

    def turn_lamp_off(self) -> None:
        if self.lamp.is_on():
            self.lamp.turn_off()
