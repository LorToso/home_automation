import datetime

from input_boolean import InputBoolean


class NightModeBoolean(InputBoolean):

    no_longer_night_time = datetime.time(12, 0, 0)
    definitely_night_time = datetime.time(1, 0, 0)

    def initialize(self) -> None:
        super().initialize()
        #self.run_daily(self.no_longer_night, NightModeBoolean.no_longer_night_time)
        #self.run_daily(self.definitely_night, NightModeBoolean.definitely_night_time)

    def no_longer_night(self, kwargs):
        self.turn_off()

    def definitely_night(self, kwargs):
        self.turn_on()
