import reflex as rx

from chemicy.backend.item.ItemDto import ItemDto

from chemicy.search.dialogs.item_state import ItemState
from chemicy.search.search_state import SearchState
from chemicy.session.session_state import SessionState


def _editable_dialog(item: ItemDto):
    return rx.dialog.root(
        rx.dialog.trigger(rx.link(item.name), on_click=ItemState.load_item(item)),
        rx.dialog.content(
            rx.dialog.title(item.name),
            rx.dialog.description(
                rx.flex(
                    rx.cond(ItemState.edit_mode,
                        rx.card(
                            rx.heading("Nazwa odczynnika"),
                            rx.input(
                                placeholder="Enter text...",
                                value=ItemState.item.name,
                                on_change=ItemState.update_name
                            ),
                            # rx.text(item.name),

                            rx.heading("Ilość"),
                            rx.input(
                                placeholder="Enter text...",
                                value=ItemState.item.amount,
                                on_change=ItemState.update_amount),
                            rx.hstack(
                                rx.vstack(
                                    rx.heading("Zagrożenia P", size="3"),
                                    rx.list.unordered(
                                        rx.foreach(ItemState.item.p_codes, lambda p: rx.list.item(p)),
                                    ),
                                ),
                                rx.vstack(
                                    rx.heading("Zagrożenia H", size="3"),
                                    rx.list.unordered(
                                        rx.foreach(ItemState.item.h_codes, lambda h: rx.list.item(h)),
                                    )
                                ),
                            ),
                            width="50%",
                        ),
                        rx.card(
                            rx.heading("Nazwa odczynnika"),
                            rx.text(item.name),
                            rx.heading("Ilość"),
                            rx.text(item.amount),
                            rx.hstack(
                                rx.vstack(
                                    rx.heading("Zagrożenia P", size="3"),
                                    rx.list.unordered(
                                        rx.foreach(ItemState.item.p_codes, lambda p: rx.list.item(p)),
                                    ),
                                ),
                                rx.vstack(
                                    rx.heading("Zagrożenia H", size="3"),
                                    rx.list.unordered(
                                        rx.foreach(ItemState.item.h_codes, lambda h: rx.list.item(h)),
                                    )
                                ),
                            ),
                            width="50%",
                        ),
                    ),

                    rx.cond(ItemState.edit_mode,
                        rx.card(
                            rx.heading("Numer CAS"),
                            rx.input(
                                placeholder="Enter text...",
                                value=ItemState.item.cas,
                                on_change=ItemState.update_cas),
                            rx.heading("Właściciel"),
                            rx.select(ItemState.user_names,
                                      value=ItemState.selected_username,
                                      on_change=ItemState.update_owner),
                            rx.heading("Pokój"),
                            rx.select(ItemState.room_names,
                                      value=ItemState.selected_room,
                                      on_change=ItemState.update_room),
                            rx.heading("Miejsce"),
                            rx.select(ItemState.location_names,
                                      value=ItemState.selected_location,
                                      on_change=ItemState.update_location),
                            rx.heading("Status"),
                            rx.text(ItemState.item.status),
                            rx.heading("Producent"),
                            rx.input(
                                placeholder="Enter text...",
                                value=ItemState.item.producent,
                                on_change=ItemState.update_producent),

                            width="50%",
                        ),
                        rx.card(
                            rx.heading("Numer CAS"),
                            rx.text(item.cas),
                            rx.heading("Właściciel"),
                            rx.text(item.owner_name),
                            rx.heading("Pokój"),
                            rx.text(item.location.room.name),
                            rx.heading("Miejsce"),
                            rx.text(item.location.name),
                            rx.heading("Status"),
                            rx.text(item.status),
                            rx.heading("Producent"),
                            rx.text(item.producent),

                            width="50%",
                        ),
                    ),


                    spacing="2",
                    direction="row",
                ),
                rx.cond(ItemState.editable & ~ItemState.edit_mode,
                        rx.hstack(
                            rx.button("Edytuj", size= "3", on_click=ItemState.edit_btn, margin_top="5px", margin_bottom = "10px"),
                        rx.button("Drukuj Etykietę", size = "3", on_click=ItemState.print_label, margin_left = "5px", margin_top="5px", margin_bottom = "10px")),
                        None),
            ),

            rx.dialog.close(
                rx.hstack(
                    rx.button("Anuluj", size="3"),
                    rx.cond(ItemState.edit_mode,
                            rx.button("Zapisz zmiany", size="3"),
                            None),
                )
            ),
        ),
    )


def _default_dialog(item: ItemDto):
    return rx.dialog.root(
        rx.dialog.trigger(rx.link(item.name)),
        rx.dialog.content(
            rx.dialog.title(item.name),
            rx.dialog.description(
                rx.flex(
                    # rx.card(
                    #     rx.heading("Nazwa odczynnika"),
                    #     rx.text(item.name),
                    #     rx.heading("Ilość"),
                    #     rx.text(item.amount),
                    #     rx.hstack(
                    #         rx.vstack(
                    #             rx.heading("Zagrożenia P", size="3"),
                    #             rx.list.unordered(
                    #                 rx.foreach(ItemState.item.p_codes, lambda p: rx.list.item(p)),
                    #             ),
                    #         ),
                    #         rx.vstack(
                    #             rx.heading("Zagrożenia H", size="3"),
                    #             rx.list.unordered(
                    #                 rx.foreach(ItemState.item.h_codes, lambda h: rx.list.item(h)),
                    #             )
                    #         ),
                    #     ),
                    #     width="50%",
                    # ),
                    # rx.card(
                    #     rx.heading("Numer CAS"),
                    #     rx.text(item.cas),
                    #     rx.heading("Właściciel"),
                    #     rx.text(item.owner_name),
                    #     rx.heading("Pokój"),
                    #     rx.text(item.location.room.name),
                    #     rx.heading("Miejsce"),
                    #     rx.text(item.location.name),
                    #     rx.heading("Status"),
                    #     rx.text(item.status),
                    #     # rx.heading("Jednostka Organizacyjna"),
                    #     # rx.text(item.group),
                    #     rx.heading("Producent"),
                    #     rx.text(item.producent),
                    #
                    #
                    #     width="50%",
                    # ),
                    spacing="2",
                    direction="row",
                )
            ),
            rx.dialog.close(
                rx.hstack(
                    rx.button("Wyjdź", size="3"),
                )
            ),
        ),
    )


def item_dialog(item: ItemDto):
    return _editable_dialog(item)
