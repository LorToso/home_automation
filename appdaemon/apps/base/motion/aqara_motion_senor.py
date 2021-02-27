from typing import Any, Dict, Callable, List, Union

import appdaemon.plugins.hass.hassapi as hass

from base.input_boolean.boolean_set import BooleanSet


class AqaraMotionSensor:

    def __init__(
            self,
            entity_id: str,
            controller: hass.Hass,
            callback: Callable[[str, str, int], None],
            activation_booleans: Union[str, List[str]]
    ):
        self.listened_durations = set()
        self.motion_state = "off"
        self.entity_id = entity_id
        self.controller = controller
        self.callback = callback
        self.boolean_set = BooleanSet(controller, activation_booleans)

    def listen_to(self, duration: int, **kwargs):

        if duration in self.listened_durations:
            self.controller.log(f"Already listening to duration {duration}. Ignoring.")
            return
        else:
            self.listened_durations.add(duration)

        self.controller.log(f"listening to state_changes for id {self.entity_id} with duration {duration}")
        self.controller.listen_state(
            self.on_state,
            entity=self.entity_id,
            immediate=True,
            duration=duration,
            state_duration=duration,
            **kwargs
        )

    def on_state(self, entity, attribute, old, new, kwargs: Dict[str, Any]) -> None:
        state_duration = kwargs['state_duration']
        self.motion_state = new

        if old is None:
            old = "off"

        if not self.boolean_set.is_active():
            self.boolean_set.log_states()
            self.controller.log(f"Skipping action.")
            return

        self.callback(old, new, state_duration)

