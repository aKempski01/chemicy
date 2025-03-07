import reflex as rx
from chemicy.main.widgets.login_state import LoginState

def login_widget():
    return rx.card(
        rx.vstack(
    rx.heading('Nazwa użytkownika'),

        rx.input(
            placeholder="...",
            value = LoginState.email,
            on_change=LoginState.set_email,
       ),
        rx.heading('Hasło'),
        rx.input(
            placeholder="...",
            type="password",
            value=LoginState.password,
            on_change=LoginState.set_password,
        ),
        rx.hstack(
            rx.button("Zaloguj", on_click=LoginState.login_btn_clicked),
            rx.button("Zarejestruj", on_click=LoginState.register_btn_clicked),
        )
    ),
    width="36%",
    align="center",
)