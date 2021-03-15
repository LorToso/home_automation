from typing import Dict, List

import appdaemon.plugins.hass.hassapi as hass


class ActionableNotification:

    YES_NO_ACTION = [
        {
            "title": "Yes",
            "action": "Yes"
        },
        {
            "title": "No",
            "action": "No"
        },
    ]

    @staticmethod
    def listen_to_notifications(
            controller: hass.Hass,
            callback
    ) -> None:
        controller.listen_event(callback, event="mobile_app_notification_action")

    @staticmethod
    def send_notification(
        controller: hass.Hass,
        title: str,
        message: str,
        actions: List[Dict[str, str]]
    ) -> None:
        controller.log(f"Sending actionable phone notification with message [{message}]")
        controller.notify(
            title=title,
            message=message,
            data={
                "actions": actions
            }
        )
