import hassapi as hass
import datetime


class BedroomLamp(hass.Hass):

  def initialize(self):
    pass

   # Our callback function will be called by the scheduler every day at 7pm
  def run_daily_callback(self, kwargs):
    # Call to Home Assistant to turn the porch light on
    self.turn_on("light.porch")