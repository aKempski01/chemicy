import reflex as rx

from rxconfig import config
from chemicy.main.widgets.login_widget import login_widget

def main_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.flex(
            rx.heading("Chemiczny inwentarz", size="9"),
            login_widget(),
            direction="column",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )