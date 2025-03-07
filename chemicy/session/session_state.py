from typing import Optional

import reflex as rx

from chemicy.backend.user.UserDto import UserDto
from chemicy.backend.user.UserService import validate_user, get_user_by_email


class SessionState(rx.State):
    user: Optional[UserDto] = None

    def validate_admin(self):
        if self.user is None or self.user.rights == "None":
            self.log_out()

    def validate_user(self) -> None:
        if self.user is None:
            self.log_out()

    def log_in(self, email: str, password: str) -> bool:
        if validate_user(email, password):
            self.user = get_user_by_email(email)
            print(self.user)
            return True

        return False

    def log_out(self):
        self.user = None
        return rx.redirect("/")
