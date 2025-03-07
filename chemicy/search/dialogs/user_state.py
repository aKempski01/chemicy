from typing import Optional

import reflex as rx

from chemicy.backend.user.UserDto import UserDto
from chemicy.backend.user.UserService import get_all_users
# from chemicy.search.router import get_users


class UserState(rx.State):

    user: Optional[UserDto] = None

    def init(self, user_id: int):
        users = get_all_users()
        self.user = [u for u in users if u.id == user_id][0]
