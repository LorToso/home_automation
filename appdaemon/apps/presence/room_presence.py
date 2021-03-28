from typing import List

import appdaemon.plugins.hass.hassapi as hass

from presence.room import Room


class RoomPresence(hass.Hass):

    entity_id: str = ""
    rooms: List[Room]

    def initialize(self) -> None:

        self.rooms = [Room(self, **room) for room in self.args["rooms"]]

        for room in self.rooms:
            self.listen_state(self.on_motion, entity=room.motion_sensor, immediate=True)
            self.listen_state(self.on_presence, entity=room.presence_boolean, immediate=True)

    def on_presence(self, entity, attribute, old, new_state, kwargs) -> None:
        new_presence_room = self.find_room_by_presence_boolean(entity)
        new_presence_room.state = new_state
        self.handle_presence(new_state, new_presence_room)

    def on_motion(self, entity, attribute, old, new_state, kwargs) -> None:
        new_presence_room = self.find_room_by_motion_sensor(entity)
        self.handle_presence(new_state, new_presence_room)

    def handle_presence(self, new_state, new_presence_room):
        if new_state == "on":
            self.log(f"Found presence in {new_presence_room.presence_boolean}")
            new_presence_room.set_presence(True)

            if not self.guest_mode_is_on():
                self.turn_off_presence_in_all_other_rooms(new_presence_room)

        elif new_state == "off":
            if self.guest_mode_is_on():
                if len(self.get_present_rooms()) > 1:
                    new_presence_room.set_presence(False)

    def find_room_by_motion_sensor(self, entity):
        return [room for room in self.rooms if room.motion_sensor == entity][0]

    def find_room_by_presence_boolean(self, entity):
        return [room for room in self.rooms if room.presence_boolean == entity][0]

    def guest_mode_is_on(self) -> bool:
        return self.get_state(self.args["guest_mode_boolean"]) == "on"

    def get_present_rooms(self) -> List[Room]:
        return [room for room in self.rooms if room.is_present()]

    def turn_off_presence_in_all_other_rooms(self, new_presence_room):
        for other_room in [room for room in self.get_present_rooms() if not room == new_presence_room]:
            self.log(f"Deactivating presence in {other_room.presence_boolean}")
            other_room.set_presence(False)
