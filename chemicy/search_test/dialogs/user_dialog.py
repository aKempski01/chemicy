import reflex as rx

from chemicy.search_test.dialogs.user_state import UserState


def user_dialog(user_id: int, user_name: str):
    return rx.dialog.root(
        rx.dialog.trigger(rx.link(user_name), on_click=UserState.init(user_id)),
        rx.dialog.content(
            rx.dialog.title(UserState.user.surname + "  " + UserState.user.name),
            rx.dialog.description(
                rx.flex(
                    rx.card(
                        rx.heading("Imię i nazwisko", size="3"),
                        rx.text(UserState.user.surname),
                        rx.text(UserState.user.name),
                        rx.heading("Zespół", size="3"),
                        rx.text(UserState.user.group),
                        width="50%"
                    ),
                    rx.card(
                        rx.heading("Dane kontaktowe"),

                        rx.heading("email", size="3"),
                        rx.text(UserState.user.email),

                        rx.heading("telefon", size="3"),
                        rx.text(UserState.user.phone),

                        rx.heading("numer pokoju", size="3"),
                        rx.text(UserState.user.room),
                        width = "50%"
                    ),
                    spacing="2",
                    direction="row",
                )
            ),
            rx.dialog.close(
                rx.button("Wyjdź", size="3"),
            ),
        ),
    )
