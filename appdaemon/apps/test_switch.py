from typing import Any, Optional

from base.switches.default_tradfri_switch import DefaultTradfriSwitch


class TestSwitch(DefaultTradfriSwitch):

    thing: Optional[Any] = None

    def on_left_clicked(self):
        self.thing.set_volume(0.5)
        #self.thing.say(
        #    "This is a test",
        #    "en"
        #)
        self.thing.join_group()

    def initialize(self) -> None:
        self.thing = self.get_app("bath_room_speaker")

        super().initialize()
