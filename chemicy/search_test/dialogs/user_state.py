from typing import Optional

import reflex as rx

from chemicy.models.user import UserModel
from chemicy.search_test.router import get_users


class UserState(rx.State):

    user: Optional[UserModel] = None

    def init(self, user_id: int):
        users = get_users()
        self.user = [u for u in users if u.id == user_id][0]
