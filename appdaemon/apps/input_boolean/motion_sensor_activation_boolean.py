from helpers import safe_get_app
from input_boolean import InputBoolean
from sonos_speaker import SonosSpeaker
from config import strings


class MotionSensorActivationBoolean(InputBoolean):

    speaker: SonosSpeaker

    def initialize(self) -> None:
        self.speaker = safe_get_app(self, self.args['speakers'])
        super().initialize()

    def on_state(self, old_state: bool, new_state: bool):
        if self.speaker.is_playing():
            return

        if old_state == 'off' and new_state == 'on':
            message = strings.motion_sensor_activated_message[0]
            language = strings.motion_sensor_activated_message[1]
            self.speaker.say(message, language)
        elif old_state == 'on' and new_state == 'off':
            message = strings.motion_sensor_deactivated_message[0]
            language = strings.motion_sensor_deactivated_message[1]
            self.speaker.say(message, language)
