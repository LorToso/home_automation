from typing import Any, Dict, Optional

from base.lamps.hue_lamp import HueLamp
from night_mode_boolean import NightModeBoolean


class BedRoomNightLamp(HueLamp):

    # This should be an enum
    AVAILABLE_COLORS: Dict[str, Dict[str, Any]] = {
        "red": {
            "rgb_color": [255, 53, 53],
            "brightness": HueLamp.MAX_BRIGHTNESS
        },
        "warm_white": {
            "color_temp": 333,
            "brightness": 200
        },
    }
    next_color: Optional[str]
    color: str
    listened_attributes = set([item for sublist in [color.keys() for color in AVAILABLE_COLORS.values()] for item in sublist])

    def initialize(self) -> None:
        super().initialize()
        self.color = "unknown"
        self.next_color = None

        self.run_daily(self.on_schedule, NightModeBoolean.no_longer_night_time)
        for attribute in BedRoomNightLamp.listened_attributes:
            self.listen_state(self.on_color_change, entity=self.entity_id, attribute=attribute, immediate=True)

    def on_color_change(self, entity, attribute, old, new, kwargs):
        # This is not ideal, but works for now
        for color_name, values in BedRoomNightLamp.AVAILABLE_COLORS.items():
            if attribute in values and values[attribute] == new:
                self.color = color_name
                self.log(f"New color is: {color_name}")
                return
        self.color = "unknown"
        self.log(f"New color is: {self.color}")

    def on_schedule(self, kwargs):
        self.next_color = "warm_white"

    def turn_on(self, **kwargs) -> None:
        if self.next_color is None:
            super().turn_on(**kwargs)
        else:
            super().turn_on(**self.AVAILABLE_COLORS[self.next_color])
            self.next_color = None

    def toggle(self, **kwargs) -> None:
        if self.is_off():
            self.turn_on(**kwargs)
        else:
            self.turn_off(**kwargs)

    def set_color(self, color: str) -> None:
        self.log(f"setting color {color} to lamp {self.entity_id}")
        self.turn_on(**self.AVAILABLE_COLORS[color])

    def toggle_scene(self):
        color_names = list(self.AVAILABLE_COLORS.keys())
        try:
            index = color_names.index(self.color)
        except ValueError:
            index = 0

        new_color = color_names[(index + 1) % len(color_names)]
        self.log(f"New color is: {new_color}")
        self.set_color(new_color)
