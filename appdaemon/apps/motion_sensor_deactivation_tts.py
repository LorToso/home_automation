from typing import Dict

import appdaemon.plugins.hass.hassapi as hass

import constants
from base.tts.TTS import TTS


class MotionSensorDeactivationTTS(hass.Hass):

    activation_pairs: Dict[str, str] = {
        constants.kitchen_motion_activation_boolean:
            constants.kitchen_speaker,
        constants.bath_room_motion_activation_boolean:
            constants.bath_room_speaker,
    }

    def initialize(self) -> None:

        for input_boolean_entity_id in self.activation_pairs.keys():
            self.listen_state(self.on_state_change, entity=input_boolean_entity_id, immediate=False)

    def on_state_change(self, entity, attribute, old, new, kwargs) -> None:

        target_speaker = self.activation_pairs[entity]

        if new == 'on':
            message = constants.motion_sensor_activated_message[0]
            language = constants.motion_sensor_activated_message[1]
        else:
            message = constants.motion_sensor_deactivated_message[0]
            language = constants.motion_sensor_deactivated_message[1]

        self.log(f'Sending message [{message}] in language [{language}] to speaker [{target_speaker}]')
        TTS(self).say(target_speaker, message, language)
