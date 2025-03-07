import reflex as rx
from chemicy.register.register_state import RegisterState

@rx.page(route="/register", on_load=RegisterState.init_state)
def register_page():
    return rx.container(
        rx.heading("Rejestracja", size="9"),
        rx.flex(
            rx.vstack(
                rx.heading("Email", size="5"),
                rx.input(
                    placeholder="...",
                    value=RegisterState.user.email,
                    on_change=RegisterState.set_email,

                )
            ),
            rx.vstack(
                rx.heading("Hasło", size="5"),
                rx.input(
                    placeholder="...",
                    type="Password",
                    value=RegisterState.user.password,
                    on_change=RegisterState.set_password,
                )
            ),
            rx.vstack(
                rx.heading("Imię", size="5"),
                rx.input(
                    placeholder="...",
                    value=RegisterState.user.name,
                    on_change=RegisterState.set_name,
                )
            ),

            rx.vstack(
                rx.heading("Nazwisko", size="5"),
                rx.input(
                    placeholder="...",
                    value=RegisterState.user.surname,
                    on_change=RegisterState.set_surname,
                )
            ),

            rx.vstack(
                rx.heading("Wydział", size="5"),
                rx.select(
                    RegisterState.faculty_names,
                    value=RegisterState.user.faculty,
                    on_change=RegisterState.set_faculty,
                )
            ),

            rx.vstack(
                rx.heading("Katedra", size="5"),
                rx.select(
                    RegisterState.departments,
                    value=RegisterState.user.department,
                    on_change=RegisterState.set_department,
                )
            ),

            rx.vstack(
                rx.heading("Telefon", size="5"),
                rx.text("(opcjonalne)"),
                rx.input(
                    placeholder="...",
                    value=RegisterState.user.phone,
                    on_change=RegisterState.set_phone,
                )
            ),

            rx.vstack(
                rx.heading("Numer biura", size="5"),
                rx.text("(opcjonalne)"),
                rx.input(
                    placeholder="...",
                    value=RegisterState.user.office_room,
                    on_change=RegisterState.set_office_room,
                )
            ),

            rx.vstack(
                rx.heading("Strona internetowa", size="5"),
                rx.text("(opcjonalne)"),
                rx.input(
                    placeholder="...",
                    value=RegisterState.user.website,
                    on_change=RegisterState.set_website,
                )
            ),
            spacing = "5",
            flex_wrap = "wrap",
            width = "100%",
        ),
        rx.button("Wyślij formularz rejestracyjny", on_click=RegisterState.register_btn_clicked, margin_top="2em", disabled=~RegisterState.register_valid),
    )
