import reflex as rx

from chemicy.models.reagent import ReagentModel
from chemicy.search_test.dialogs.reagent_dialog import reagent_dialog
from chemicy.search_test.dialogs.user_dialog import user_dialog
from chemicy.search_test.search_state import SearchState


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
            SearchState.user_reagents,
            lambda reagent: rx.table.row(
                rx.table.row_header_cell(reagent_dialog(reagent)),
                rx.table.cell(reagent.place.room.room_name),
                rx.table.cell(reagent.place.place_name),
                rx.table.cell(user_dialog(reagent.owner_id, reagent.owner_name)),
                rx.table.cell(reagent.status),
                )
            ),
        width="100%",
        )
    )


@rx.page(route="/search_2", on_load=SearchState.init_state)
def search_page():
    return rx.container(
        get_table(),
    )
