from base.lamps.hue_lamp import HueLamp


class BedRoomNightLamp(HueLamp):

    AVAILABLE_COLORS = {
        "red": {
            "color_temp": 499,
            "brightness": HueLamp.MAX_BRIGHTNESS
        },
        "warm_white": {
            "color_temp": 333,
            "brightness": HueLamp.MAX_BRIGHTNESS
        },
    }

    def set_color(self, color: str) -> None:
        self.log(f"setting color {color} to lamp {self.entity_id}")
        self.turn_on(**self.AVAILABLE_COLORS[color])
