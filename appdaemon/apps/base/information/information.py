import appdaemon.plugins.hass.hassapi as hass


def it_is_dark(controller: hass.Hass) -> bool:
    if controller.sun_down():
        return True

    weather = get_weather(controller)
    return weather not in ["sunny", "partlycloudy"]


def get_weather(controller: hass.Hass) -> str:
    return controller.get_state(entity_id='weather.home')
