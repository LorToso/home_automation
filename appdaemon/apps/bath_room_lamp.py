from datetime import time

from base.lamps.TimeDimmedLamp import TimeDimmedLamp, TimeWindowBrightness


class BathRoomLamp(TimeDimmedLamp):
    default_brightness = 254
    time_window_brightnesses = [
        TimeWindowBrightness(
            start_time=time(hour=0, minute=0),
            end_time=time(hour=7, minute=0),
            brightness=int(TimeDimmedLamp.MAX_BRIGHTNESS * 0.2)  # 20%
        ),
        TimeWindowBrightness(
            start_time=time(hour=7, minute=0),
            end_time=time(hour=10, minute=0),
            brightness=int(TimeDimmedLamp.MAX_BRIGHTNESS * 0.5)  # 50%
        ),
        TimeWindowBrightness(
            start_time=time(hour=10, minute=0),
            end_time=time(hour=20, minute=0),
            brightness=int(TimeDimmedLamp.MAX_BRIGHTNESS * 0.9)  # 90%
        ),
        TimeWindowBrightness(
            start_time=time(hour=20, minute=0),
            end_time=time(hour=23, minute=59, second=59),
            brightness=int(TimeDimmedLamp.MAX_BRIGHTNESS * 0.5)  # 50%
        ),
    ]



