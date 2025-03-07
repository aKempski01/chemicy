from typing import Optional, List

import reflex as rx

from chemicy.models.reagent import ReagentModel
from chemicy.models.room_place import RoomModel, PlaceModel
from chemicy.models.user import UserModel
from chemicy.search_test.router import get_users, get_rooms, get_places_for_room_id

class ReagentState(rx.State):
    reagent: Optional[ReagentModel]

    owner: Optional[UserModel]
    users: List[UserModel]

    user_names: List[str]
    selected_username: str

    rooms: List[RoomModel]
    room_names: List[str]
    selected_room: str

    places: List[PlaceModel]
    place_names: List[str]
    selected_place: str

    edit_dialog_open = False

    def load_reagent(self, reagent: ReagentModel):
        self.reagent = reagent
        self.users = get_users()
        self.owner = [u for u in self. users if u.id == reagent.owner_id][0]
        self.user_names = [u.surname + "  " + u.name for u in self.users]
        self.selected_username = self.owner.surname + "  " + self.owner.name

        self.rooms = get_rooms()
        self.room_names = [r.room_name for r in self.rooms]
        self.selected_room = self.reagent.place.room.room_name

        self.places = get_places_for_room_id(reagent.place.room.id)
        self.place_names = [p.place_name for p in self.places]
        self.selected_place = self.reagent.place.place_name


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

        self.places = get_places_for_room_id([r.id for r in self.rooms if r.room_name == room_name][0])
        self.place_names = [p.place_name for p in self.places]
        self.selected_place = self.place_names[0]

    def update_place(self, place_name: str):
        self.selected_place = place_name

    def update_rights(self, rights: str):
        self.reagent.rights = rights

    def update_producent(self, producent_name: str):
        self.reagent.producent = producent_name

