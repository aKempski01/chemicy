from typing import Optional, List

import reflex as rx

from chemicy.backend.user.UserDto import UserDto
from chemicy.backend.item.ItemDto import ItemDto

from chemicy.backend.item.ItemService import get_all_items_db
from chemicy.backend.user.UserService import get_all_user_db, get_logged_user

from chemicy.session.session_state import SessionState

class SearchState(SessionState):
    user_to_be_displayed: Optional[UserDto]
    users: List[UserDto]
    user_items: List[ItemDto]

    def init_state(self) -> None:
        self.user_items = get_all_items_db()
        self.users = get_all_user_db()


        for r in self.user_items:
            r.owner_name = [u.surname + '  ' + u.name for u in self.users if u.id == r.owner_id][0]


    @rx.event
    def set_user_to_be_displayed_by_id(self, user_id: int):
        self.user_to_be_displayed = [u for u in self.users if u.id == user_id][0]

