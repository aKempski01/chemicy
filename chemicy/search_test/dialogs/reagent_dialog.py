import reflex as rx

from chemicy.models.reagent import ReagentModel
from chemicy.search_test.dialogs.reagent_state import ReagentState
from chemicy.search_test.search_state import SearchState


def _editable_dialog(reagent: ReagentModel):
    return rx.dialog.root(
        rx.dialog.trigger(rx.link(reagent.name), on_click=ReagentState.load_reagent(reagent)),
        rx.dialog.content(
            rx.dialog.title(reagent.name),
            rx.dialog.description(
                rx.flex(
                    rx.card(
                        rx.heading("Nazwa odczynnika"),
                        rx.input(
                            placeholder="Enter text...",
                            value=ReagentState.reagent.name,
                            on_change=ReagentState.update_name),
                        rx.heading("Ilość"),
                        rx.input(
                            placeholder="Enter text...",
                            value=ReagentState.reagent.amount,
                            on_change=ReagentState.update_amount),
                        rx.hstack(
                            rx.vstack(
                                rx.heading("Zagrożenia P", size="3"),
                                rx.list.unordered(
                                    rx.foreach(ReagentState.reagent.P_class, lambda p: rx.list.item(p)),
                                ),
                            ),
                            rx.vstack(
                                rx.heading("Zagrożenia H", size="3"),
                                rx.list.unordered(
                                    rx.foreach(ReagentState.reagent.H_class, lambda h: rx.list.item(h)),
                                )
                            ),
                        ),
                        width="50%",
                    ),
                    rx.card(
                        rx.heading("Numer CAS"),
                        rx.input(
                            placeholder="Enter text...",
                            value=ReagentState.reagent.cas,
                            on_change=ReagentState.update_cas),
                        rx.heading("Właściciel"),
                        rx.select(ReagentState.user_names,
                                  value=ReagentState.selected_username,
                                  on_change=ReagentState.update_owner),
                        rx.heading("Pokój"),
                        rx.select(ReagentState.room_names,
                                  value=ReagentState.selected_room,
                                  on_change=ReagentState.update_room),
                        rx.heading("Miejsce"),
                        rx.select(ReagentState.place_names,
                                  value=ReagentState.selected_place,
                                  on_change=ReagentState.update_place),
                        rx.heading("Status"),
                        rx.text(ReagentState.reagent.status),
                        rx.heading("Dostęp"),
                        rx.select(["Open", "Private"],
                                  value=ReagentState.reagent.rights,
                                  on_change=ReagentState.update_rights),
                        rx.text(reagent.rights),
                        rx.select(["RCH-5"], value=ReagentState.reagent.group),
                        rx.heading("Producent"),
                        rx.input(
                            placeholder="Enter text...",
                            value=ReagentState.reagent.producent,
                            on_change=ReagentState.update_producent),

                        width="50%",
                    ),
                    spacing="2",
                    direction="row",
                )
            ),
            rx.dialog.close(
                rx.hstack(
                    rx.button("Zapisz zmiany", size="3"),
                    rx.button("Anuluj", size="3"),
                )
            ),
        ),
    )


def _default_dialog(reagent: ReagentModel):
    return rx.dialog.root(
        rx.dialog.trigger(rx.link(reagent.name)),
        rx.dialog.content(
            rx.dialog.title(reagent.name),
            rx.dialog.description(
                rx.flex(
                    rx.card(
                        rx.heading("Nazwa odczynnika"),
                        rx.text(reagent.name),
                        rx.heading("Ilość"),
                        rx.text(reagent.amount),
                        rx.hstack(
                            rx.vstack(
                                rx.heading("Zagrożenia P", size="3"),
                                rx.list.unordered(
                                    rx.foreach(ReagentState.reagent.P_class, lambda p: rx.list.item(p)),
                                ),
                            ),
                            rx.vstack(
                                rx.heading("Zagrożenia H", size="3"),
                                rx.list.unordered(
                                    rx.foreach(ReagentState.reagent.H_class, lambda h: rx.list.item(h)),
                                )
                            ),
                        ),
                        width="50%",
                    ),
                    rx.card(
                        rx.heading("Numer CAS"),
                        rx.text(reagent.cas),
                        rx.heading("Właściciel"),
                        rx.text(reagent.owner_name),
                        rx.heading("Pokój"),
                        rx.text(reagent.place.room.room_name),
                        rx.heading("Miejsce"),
                        rx.text(reagent.place.place_name),
                        rx.heading("Status"),
                        rx.text(reagent.status),
                        rx.heading("Dostęp"),
                        rx.text(reagent.rights),
                        rx.heading("Jednostka Organizacyjna"),
                        rx.text(reagent.group),
                        rx.heading("Producent"),
                        rx.text(reagent.producent),


                        width="50%",
                    ),
                    spacing="2",
                    direction="row",
                )
            ),
            rx.dialog.close(
                rx.hstack(
                    # rx.cond(
                    #     reagent.owner_id == SearchState.user.id,
                    #     rx.button("Edytuj", on_click=ReagentState.open_edit_dialog(reagent), size="3"),
                    #     None,
                    # ),
                    rx.button("Wyjdź", size="3"),
                )
            ),
        ),
        width="100%",
    )


def reagent_dialog(reagent: ReagentModel):
    return rx.match(
            reagent.owner_id,
            (SearchState.user.id, _editable_dialog(reagent)),
            _default_dialog(reagent),
        )


