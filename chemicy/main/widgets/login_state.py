import reflex as rx
from chemicy.backend.user.UserService import validate_user
from chemicy.session.session_state import SessionState



class LoginState(SessionState):
    email: str = ""
    password: str = ""

    def login_btn_clicked(self):
        if validate_user(self.email, self.password):
            if self.log_in(self.email, self.password):
                return rx.redirect("/search")
            else:
                return rx.toast.error("Internal Server Error")
        else:
            return rx.toast.error("Błędna nazwa użytkownika, lub hasło")

    def register_btn_clicked(self):
        return rx.redirect("/register")


    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password
