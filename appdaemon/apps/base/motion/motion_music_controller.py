import appdaemon.plugins.hass.hassapi as hass

from base.motion.aqara_motion_senor import AqaraMotionSensor
from base.speaker.sonos_speaker import SonosSpeaker


class MotionMusicController(hass.Hass):

    motion_sensor: AqaraMotionSensor
    speaker: SonosSpeaker
    turn_off_after_seconds: int
    ignore_brightness: bool
    motion_added_speaker_in_group: bool

    def initialize(self) -> None:
        self.motion_sensor = AqaraMotionSensor(
            self.args["motion_entity_id"],
            self,
            self.on_motion_detected,
            self.args["activation_boolean"]
        )
        self.speaker: SonosSpeaker = self.get_app(self.args["speaker"])

        self.motion_added_speaker_in_group = False
        self.turn_off_after_seconds: int = self.args['turn_music_off_after_seconds']

        self.motion_sensor.listen_to(0)
        self.motion_sensor.listen_to(self.turn_off_after_seconds)


    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        if old_motion_state == 'off' and new_motion_state == 'on' and state_duration == 0:
            self.turn_music_on()

        if old_motion_state == 'on' and new_motion_state == 'off' and state_duration == self.turn_off_after_seconds:
            self.turn_music_off()

    def on_group_joined(self):
        pass

    def on_group_unjoined(self):
        pass

    def turn_music_on(self) -> None:
        self.log(f"Own speaker state: {self.speaker.state}")
        if self.speaker.is_playing():
            self.log("Already playing. Doing nothing.")
            return

        if self.speaker.speaker_group.someone_is_playing():
            self.log("Someone is playing. Joining in...")
            self.speaker.join_group()
            self.motion_added_speaker_in_group = True
        else:
            self.log("No one is playing. Staying quiet")
            self.motion_added_speaker_in_group = False

    def turn_music_off(self) -> None:
        self.log("Delayed off. Speaker unjoining group.")
        if self.speaker.is_in_group and not self.speaker.is_group_leader():
            self.speaker.unjoin_group()
            self.motion_added_speaker_in_group = False
        #else:
        #    self.log("Delayed off. Doing nothing")


