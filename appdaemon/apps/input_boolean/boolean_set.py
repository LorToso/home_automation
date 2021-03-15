from typing import Union, List, Tuple

import appdaemon.plugins.hass.hassapi as hass

from helpers import safe_get_app
from input_boolean import InputBoolean


class BooleanSet:
    NEGATION_PREFIX = "not:"

    def __init__(self, controller: hass.Hass, boolean_app_names: Union[str, List[str]]):
        self.controller = controller
        positives, negatives = self.parse_activation_boolean(controller, boolean_app_names)

        self.positives = positives
        self.negatives = negatives

    def is_active(self):
        return all([b.is_on() for b in self.positives]) and not any([b.is_on() for b in self.negatives])

    def log_states(self):
        positives_str = ', '.join(
            [f'{boolean.entity_id}: {boolean.state}' for boolean in self.positives]
        )
        negatives_str = ', '.join(
            [f'{boolean.entity_id}: {boolean.state}' for boolean in self.negatives]
        )

        full_str = f"Boolean states: Positives: [{positives_str}], Negatives: [{negatives_str}]"
        self.controller.log(full_str)

    @staticmethod
    def parse_activation_boolean(
            controller: hass.Hass,
            activation_boolean: Union[str, List[str]]
    ) -> Tuple[List[InputBoolean], List[InputBoolean]]:

        if activation_boolean is None:
            return [], []
        elif type(activation_boolean) == str:
            activation_boolean = [activation_boolean]

        assert type(activation_boolean) == list

        positives = [
            b for b in activation_boolean if not b.startswith(BooleanSet.NEGATION_PREFIX)
        ]
        negatives = [
            b for b in activation_boolean if b not in positives
        ]
        controller.log(f"Positives: {positives}")
        controller.log(f"Negatives: {negatives}")

        positives = [
            safe_get_app(controller, b) for b in positives
        ]
        negatives = [
            safe_get_app(controller, b[len(BooleanSet.NEGATION_PREFIX):]) for b in negatives
        ]
        return positives, negatives
