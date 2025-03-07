from typing import Optional, List

import reflex as rx

from chemicy.models.reagent import ReagentModel
from chemicy.models.user import UserModel

from chemicy.search_test.router import get_reagents, get_users, get_logged_user



class Search2State(rx.State):
    user: Optional[UserModel]
    user_to_be_displayed: Optional[UserModel]
    users: List[UserModel]
    user_reagents: List[ReagentModel]


    def init_state(self) -> None:
        self.user_reagents = get_reagents()
        self.users = get_users()
        self.user = get_logged_user()

        for r in self.user_reagents:
            r.owner_name = [u.surname + '  ' + u.name for u in self.users if u.id == r.owner_id][0]

    @rx.event
    def set_user_to_be_displayed_by_id(self, user_id: int):
        self.user_to_be_displayed = [u for u in self.users if u.id == user_id][0]

