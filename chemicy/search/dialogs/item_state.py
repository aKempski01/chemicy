from typing import Optional, List

import reflex as rx

from chemicy.backend.item.ItemDto import ItemDto
from chemicy.backend.LocationRoom.LocationRoomDto import LocationDto, RoomDto
from chemicy.backend.user.UserDto import UserDto
from chemicy.backend.user.UserService import get_all_users
from chemicy.backend.LocationRoom.LocationRoomService import get_rooms, get_locations_for_room_id
from chemicy.session.session_state import SessionState


# from chemicy.search_test.router import get_rooms, get_places_for_room_id

class ItemState(SessionState):
    item: Optional[ItemDto]

    owner: Optional[UserDto]
    users: List[UserDto]

    user_names: List[str]
    selected_username: str

    rooms: List[RoomDto]
    room_names: List[str]
    selected_room: str

    locations: List[LocationDto]
    location_names: List[str]
    selected_location: str

    edit_mode: bool = False
    editable: bool = False

    def load_item(self, item: ItemDto):
        self.item = item
        self.users = get_all_users()
        self.owner = [u for u in self. users if u.id == item.owner_id][0]
        self.user_names = [u.surname + "  " + u.name for u in self.users]
        self.selected_username = self.owner.surname + "  " + self.owner.name

        self.rooms = get_rooms()
        self.room_names = [r.name for r in self.rooms]
        self.selected_room = self.item.location.room.name

        self.locations = get_locations_for_room_id(item.location.room.id)
        self.location_names = [l.name for l in self.locations]
        self.selected_location = self.item.location.name

        self.edit_mode = False
        self.editable = item.owner_id == self.user.id


    def update_name(self, name: str):
        self.reagent.name = name

    def update_amount(self, amount: str):
        self.reagent.amount = amount

    def update_cas(self, cas: str):
        self.reagent.cas = cas

    def update_owner(self, owner_name: str):
        idx = [i for i in range(len(self.user_names)) if self.user_names[i] == owner_name][0]
        self.owner = self.users[idx]
        self.selected_username = self.user_names[idx]

    def update_room(self, room_name: str):
        self.selected_room = room_name

        # self.places = get_places_for_room_id([r.id for r in self.rooms if r.room_name == room_name][0])
        self.location_names = [l.name for l in self.locations]
        self.selected_location = self.location_names[0]

    def update_location(self, location_name: str):
        self.selected_location = location_name

    def update_producent(self, producent_name: str):
        self.item.producent = producent_name

    def edit_btn(self):
        self.edit_mode = True