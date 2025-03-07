import reflex as rx
from chemicy.admin.admin_state import AdminState
from chemicy.backend.LocationRoom.LocationRoomDto import RoomDto
from chemicy.admin.dialogs.location_dialogs import edit_location_dialog, delete_location_dialog, create_location_dialog


@rx.page(route="/admin", on_load=AdminState.init_state)
def admin_page():
    return rx.container(
        rx.heading("Panel Administratora", size="9"),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Użytkownicy", value="user_tab"),
                rx.tabs.trigger("Odczynniki", value="item_tab"),
                rx.tabs.trigger("Pomieszczenia", value="room_tab"),
            ),
            rx.tabs.content(
                user_table(),
                value="user_tab",
            ),
            rx.tabs.content(
                rx.text("item on tab 2"),
                value="item_tab",
            ),
            rx.tabs.content(
                room_widget(),
                value="room_tab",
            ),
        )
    )


def user_table():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Użytkownik"),
                rx.table.column_header_cell("Wydział"),
                rx.table.column_header_cell("Katedra"),
                rx.table.column_header_cell("Status"),
                rx.table.column_header_cell("Odczynniki"),
            )
        ),
        rx.table.body(
            rx.foreach(
                AdminState.users,
                lambda user: rx.table.row(
                    rx.table.row_header_cell(user.surname + " " + user.name),
                    rx.table.cell(user.department),
                    rx.table.cell(user.faculty),
                    rx.table.cell(rx.select(
                        AdminState.statuses,
                        value=user.status,
                        on_change=AdminState.update_status,
                    )),
                ),
            ),
        )
    )

def room_widget():
    return rx.accordion.root(
        rx.foreach(
            AdminState.rooms,
            lambda room: rx.accordion.item(
                value=room.id.to_string(),
                header=room.name,
                content=rx.vstack(
                    get_location_table(room),
                    create_location_dialog(room)
                ),
            )
        ),
        collapsible=True,
        width="400px",
        type="multiple",
    )

def get_location_table(room: RoomDto):
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("nazwa miejsca"),
                rx.table.column_header_cell("Edytuj"),
                rx.table.column_header_cell("Usuń"),
                rx.table.column_header_cell("pokaż odczynniki"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                room.locations,
                lambda location: rx.table.row(
                    rx.table.row_header_cell(location.name),
                    rx.table.cell(edit_location_dialog(location.id)),
                    rx.table.cell(delete_location_dialog(location.id)),
                    rx.table.cell(rx.button(rx.icon("flask-conical"), on_click=rx.toast.info("Not implemented Yet"))),
                ),
            ),
        ),
        width = "100%"
    )

