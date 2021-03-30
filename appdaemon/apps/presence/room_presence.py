from typing import List, Dict, Any

import appdaemon.plugins.hass.hassapi as hass

Room = Dict[str, Any]


class RoomPresence(hass.Hass):

    rooms: List[Room]

    def initialize(self) -> None:

        self.rooms = self.args["rooms"]

        for room in self.rooms:
            self.listen_state(self.on_motion, entity=room["motion_sensor"], immediate=True)
            self.listen_state(self.on_presence, entity=room["presence_boolean"], immediate=True)
        self.listen_state(self.on_phone_presence, entity=self.args["phone_presence_boolean"], immediate=True)

    def on_phone_presence(self, entity, attribute, old, new_state, kwargs) -> None:
        if new_state == "off":
            for room in self.rooms:
                self.set_presence(room, False)

    def on_presence(self, entity, attribute, old, new_state, kwargs) -> None:
        new_presence_room = self.find_room_by_presence_boolean(entity)
        self.handle_presence(new_state, new_presence_room)

    def on_motion(self, entity, attribute, old, new_state, kwargs) -> None:
        new_presence_room = self.find_room_by_motion_sensor(entity)
        self.handle_presence(new_state, new_presence_room)

    def handle_presence(self, new_state: str, new_presence_room: Room):
        if new_state == "on":
            self.log(f"Found presence in {new_presence_room['presence_boolean']}")
            self.set_presence(new_presence_room, True)

            if not self.guest_mode_is_on():
                self.turn_off_presence_in_all_other_rooms(new_presence_room)

        elif new_state == "off":
            if self.guest_mode_is_on():
                if len(self.get_present_rooms()) > 1:
                    self.set_presence(new_presence_room, False)

    def find_room_by_motion_sensor(self, entity: str):
        return [room for room in self.rooms if room['motion_sensor'] == entity][0]

    def find_room_by_presence_boolean(self, entity: str):
        return [room for room in self.rooms if room['presence_boolean'] == entity][0]

    def guest_mode_is_on(self) -> bool:
        return self.get_state(self.args["guest_mode_boolean"]) == "on"

    def get_present_rooms(self) -> List[Room]:
        return [room for room in self.rooms if self.is_present_in_room(room)]

    def turn_off_presence_in_all_other_rooms(self, new_presence_room: Room):
        for other_room in [room for room in self.get_present_rooms() if not room == new_presence_room]:
            self.set_presence(other_room, False)

    def set_presence(self, room: Room, active: bool):
        if active:
            self.log(f"Activating presence in {room['presence_boolean']}")
            self.turn_on(room["presence_boolean"])
        else:
            self.log(f"Deactivating presence in {room['presence_boolean']}")
            self.turn_off(room["presence_boolean"])

    def is_present_in_room(self, room):
        return self.get_state(room["presence_boolean"]) == "on"
