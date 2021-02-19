from base.input_boolean.input_boolean import InputBoolean
from base.speaker.sonos_speaker import SonosSpeaker
from config import strings


class MotionSensorActivationBoolean(InputBoolean):

    speaker: SonosSpeaker

    def initialize(self) -> None:
        self.speaker = self.get_app(self.args['speaker'])
        super().initialize()

    def on_state(self, old_state: bool, new_state: bool):
        if old_state == 'off' and new_state == 'on':
            message = strings.motion_sensor_activated_message[0]
            language = strings.motion_sensor_activated_message[1]
            self.speaker.say(message, language)
        elif old_state == 'on' and new_state == 'off':
            message = strings.motion_sensor_deactivated_message[0]
            language = strings.motion_sensor_deactivated_message[1]
            self.speaker.say(message, language)
