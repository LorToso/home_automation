from base.input_boolean.input_boolean import InputBoolean


class NightModeBoolean(InputBoolean):

    def initialize(self) -> None:
        super().initialize()
        self.run_daily(self.no_longer_night, "12:00:00")
        self.run_daily(self.definitely_night, "01:00:00")

    def no_longer_night(self, **kwargs):
        self.turn_off()

    def definitely_night(self, **kwargs):
        self.turn_off()
