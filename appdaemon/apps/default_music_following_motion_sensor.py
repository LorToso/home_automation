from typing import Optional

from base.input_boolean.input_boolean import InputBoolean
from base.speaker.SonosSpeaker import SonosSpeaker
from default_light_controlling_motion_sensor import LightControllingMotionSensor


class MusicFollowingMotionSensor(LightControllingMotionSensor):

    speaker: SonosSpeaker = None
    turn_off_after_seconds: int = 0
    activation_boolean: Optional[InputBoolean] = None
    motion_added_speaker_in_group: Optional[bool] = None
    music_follow_boolean: Optional[InputBoolean] = None

    def initialize(self) -> None:
        self.speaker = self.get_app(self.args["speaker_app_name"])
        self.music_follow_boolean = self.get_app(self.args["music_following_input_boolean_app_name"])
        super().initialize()

    def on_immediate_on(self) -> None:
        super().on_immediate_on()

        if self.music_follow_boolean.is_off():
            self.log(f"music_follow_boolean is off. Doing nothing.")
            return

        if self.speaker.is_playing():
            self.log("Already playing. Doing nothing.")
            return

        if self.speaker.speaker_group.someone_is_playing():
            self.log("Someone is playing. Joining in...")
            self.speaker.join_group()
            self.motion_added_speaker_in_group = True
        else:
            self.log("No one is playing. Staying quiet")

    def on_delayed_off(self) -> None:
        super().on_delayed_off()

        if self.music_follow_boolean.is_off():
            self.log(f"music_follow_boolean is off. Doing nothing.")
            return

        if self.motion_added_speaker_in_group:
            self.log("Delayed off. Speaker unjoining group.")
            self.speaker.unjoin_group()
            self.motion_added_speaker_in_group = False
        else:
            self.log("Delayed off. Doing nothing")
