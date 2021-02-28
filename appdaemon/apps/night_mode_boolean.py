import datetime

from base.input_boolean.input_boolean import InputBoolean


class NightModeBoolean(InputBoolean):

    def initialize(self) -> None:
        super().initialize()
        self.run_daily(self.no_longer_night, datetime.time(12, 0, 0))
        self.run_daily(self.definitely_night, datetime.time(1, 0, 0))

    def no_longer_night(self, **kwargs):
        self.turn_off()

    def definitely_night(self, **kwargs):
        self.turn_on()
