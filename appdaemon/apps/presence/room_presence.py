from typing import List, Dict, Any

import appdaemon.plugins.hass.hassapi as hass

from helpers import safe_get_app
from notifier.actionable_notification import ActionableNotification
from presence.room import Room


class RoomPresence(hass.Hass):

    entity_id: str = ""
    rooms: List[Room]

    def initialize(self) -> None:
        #self.entity_id = self.args["entity_id"]
        self.rooms = [Room(self, **room) for room in self.args["rooms"]]

        for room in self.rooms:
            self.listen_state(self.on_motion, entity=room.motion_sensor)
            #self.listen_state(self.on_presence, entity=room.presence_boolean)

    #def on_presence(self, entity, attribute, old, new, kwargs) -> None:
        #room = [room for room in self.rooms if room.presence_boolean == entity]


    def on_motion(self, entity, attribute, old, new, kwargs) -> None:
        room = [room for room in self.rooms if room.motion_sensor == entity][0]

        if new == "on":
            room.set_presence(True)
        else:
            room.set_presence(False)




