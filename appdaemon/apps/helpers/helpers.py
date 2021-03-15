from typing import Any

from appdaemon.plugins.hass import hassapi as hass


def safe_get_app(controller: hass.Hass, app_name: str) -> Any:
    app = controller.get_app(app_name)
    if app is None:
        raise AttributeError(f"Illegal app name: {app_name}")
    return app


def it_is_dark(controller: hass.Hass) -> bool:
    if controller.sun_down():
        return True

    return controller.now_is_between("sunset - 01:00:00", "sunset + 01:00:00") and not is_weather_good(controller)


def is_weather_good(controller: hass.Hass):
    weather = get_weather(controller)
    return weather in ["sunny", "partlycloudy"]


def get_weather(controller: hass.Hass) -> str:
    return controller.get_state(entity_id='weather.home')
