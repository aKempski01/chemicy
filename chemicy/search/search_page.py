import reflex as rx

from chemicy.search.dialogs.add_new_item_dialog import add_mew_item_dialog
from chemicy.search.dialogs.user_dialog import user_dialog
from chemicy.search.search_state import SearchState

from chemicy.search.dialogs.item_dialog import item_dialog
from chemicy.session.session_state import SessionState


def get_table():
    return rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Nazwa odczynnika"),
            rx.table.column_header_cell("Pomieszczenie"),
            rx.table.column_header_cell("Miejsce"),
            rx.table.column_header_cell("Właściciel"),
            rx.table.column_header_cell("Status"),
        ),
    ),

    rx.table.body(
        rx.foreach(
            SearchState.user_items,
            lambda item: rx.table.row(
                rx.table.row_header_cell(item_dialog(item)),
                rx.table.cell(item.location.room.name),
                rx.table.cell(item.location.name),
                rx.table.cell(user_dialog(item.owner_id, item.owner_name)),
                rx.table.cell(item.status),
                )
            ),
        width="100%",
        )
    )


@rx.page(route="/search", on_load=SearchState.init_state)
def search_page():
    return rx.container(
        rx.hstack(
            rx.cond(SessionState.user.rights == "Admin", rx.button("Panel Administratora", on_click=rx.redirect('/admin'))),
            add_mew_item_dialog()
        ),
        get_table(),
    )
