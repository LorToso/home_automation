from typing import Any, Dict

from base.lamps.hue_lamp import HueLamp


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
    color: str
    listened_attributes = set([item for sublist in [color.keys() for color in AVAILABLE_COLORS.values()] for item in sublist])

    def initialize(self) -> None:
        super().initialize()
        self.color = "unknown"

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
