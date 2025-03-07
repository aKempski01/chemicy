from typing import List

import reflex as rx

from chemicy.backend.LocationRoom.LocationRoomDto import RoomDto
from chemicy.backend.LocationRoom.LocationRoomService import get_rooms, get_rooms_db
from chemicy.backend.user.UserDto import UserDto
from chemicy.backend.user.UserService import get_all_user_db, get_user_statuses
from chemicy.session.session_state import SessionState


class AdminState(SessionState):
    rooms: List[RoomDto]
    users: List[UserDto]
    statuses: List[str]

    def init_state(self):
        self.validate_admin()

        self.rooms = get_rooms_db()
        self.users = get_all_user_db()
        stat = get_user_statuses()
        self.statuses = [s['name'] for s in stat]


    def update_status(self, status: str) -> None:
        pass

