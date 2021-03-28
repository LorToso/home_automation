import appdaemon.plugins.hass.hassapi as hass

from helpers import safe_get_app
from sonos_speaker import SonosSpeaker

from boolean_set import BooleanSet


class MotionMusicController(hass.Hass):
    boolean_set: BooleanSet
    speaker: SonosSpeaker
    turn_off_after_seconds: int

    def initialize(self) -> None:
        self.boolean_set = BooleanSet(self, self.args["activation_boolean"])
        self.speaker: SonosSpeaker = safe_get_app(self, self.args["speaker"])
        self.turn_off_after_seconds: int = self.args['turn_music_off_after_seconds']

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

    def on_presence_changed(self, entity, attribute, old_presence_state, new_presence_state, kwargs) -> None:
        if not self.boolean_set.is_active():
            self.boolean_set.log_states()
            self.log("Skipping action...")
            return

        if old_presence_state == 'off' and new_presence_state == 'on' and kwargs['state_duration'] == 0:
            self.turn_music_on()

        if old_presence_state == 'on' and new_presence_state == 'off' and kwargs['state_duration'] == self.turn_off_after_seconds:
            self.turn_music_off()

    def turn_music_on(self) -> None:
        self.log(f"Own speaker state: {self.speaker.state}")
        if self.speaker.is_playing():
            self.log("Already playing. Doing nothing.")
            return

        if self.speaker.speaker_group.someone_is_playing():
            self.log("Someone is playing. Joining in...")
            self.speaker.join_group()
        else:
            self.log("No one is playing. Staying quiet")

    def turn_music_off(self) -> None:
        self.log("Delayed off. Speaker unjoining group.")
        if self.speaker.is_in_group() and not self.speaker.is_group_leader():
            self.speaker.unjoin_group()
