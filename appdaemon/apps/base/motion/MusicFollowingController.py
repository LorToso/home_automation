from base.input_boolean.input_boolean import InputBoolean
from base.motion.AqaraMotionSensor import AqaraMotionSensor
from base.speaker.SonosSpeaker import SonosSpeaker


class MusicFollowingController:

    def __init__(
            self,
            controller: AqaraMotionSensor
    ):
        self.controller: AqaraMotionSensor = controller
        self.speaker: SonosSpeaker = self.controller.get_app(self.controller.args["speaker"])
        self.music_follow_boolean: InputBoolean = self.controller.get_app(self.controller.args["music_following_boolean"])
        self.turn_off_after_seconds: int = controller.args['turn_music_off_after_seconds']
        self.motion_added_speaker_in_group: bool = False

        controller.listen_to(self.turn_off_after_seconds)

    def on_motion_detected(self, old_motion_state: str, new_motion_state: str, state_duration: int):
        if old_motion_state == 'off' and new_motion_state == 'on' and state_duration == 0:
            self.turn_music_on()

        if old_motion_state == 'on' and new_motion_state == 'off' and state_duration == self.turn_off_after_seconds:
            self.turn_music_off()

    def turn_music_on(self) -> None:
        if self.music_follow_boolean.is_off():
            self.controller.log(f"music_follow_boolean is off. Doing nothing.")
            return

        if self.speaker.is_playing():
            self.controller.log("Already playing. Doing nothing.")
            return

        if self.speaker.speaker_group.someone_is_playing():
            self.controller.log("Someone is playing. Joining in...")
            self.speaker.join_group()
            self.motion_added_speaker_in_group = True
        else:
            self.controller.log("No one is playing. Staying quiet")

    def turn_music_off(self) -> None:

        if self.music_follow_boolean.is_off():
            self.controller.log(f"music_follow_boolean is off. Doing nothing.")
            return

        if self.motion_added_speaker_in_group:
            self.controller.log("Delayed off. Speaker unjoining group.")
            self.speaker.unjoin_group()
            self.motion_added_speaker_in_group = False
        else:
            self.controller.log("Delayed off. Doing nothing")
