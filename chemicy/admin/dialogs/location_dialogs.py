from typing import Optional

import reflex as rx

from chemicy.admin.admin_state import AdminState
from chemicy.backend.LocationRoom.LocationRoomDto import LocationDto, RoomDto
from chemicy.backend.LocationRoom.LocationRoomService import get_location_by_id, update_location_name, delete_location, create_location


class LocationDialogState(rx.State):
    location: Optional[LocationDto]

    def init_state(self, location_id: Optional[int] = None, room: Optional[RoomDto] = None):
        if location_id is not None:
            self.location = get_location_by_id(location_id)

        if location_id is None or self.location is None:
            self.location = LocationDto(room=room)

    def set_location_name(self, name: str):
        self.location.name = name

    def update_location_name(self):
        if self.location.name != "":
            update_location_name(self.location)

    def create_new_location(self):
        if self.location.name != "":
            create_location(self.location)

    def remove_location(self):
        if self.location is not None:
            delete_location(self.location)


def edit_location_dialog(location_id):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon("pencil"), on_click=LocationDialogState.init_state(location_id, None))),
        rx.dialog.content(
            rx.dialog.title("Edytuj wybrane miejsce"),
            rx.dialog.description(
                rx.input(
                    placeholder="Podaj nazwę miejsca",
                    on_change=LocationDialogState.set_location_name,
                    value=LocationDialogState.location.name
                ),
            ),
            rx.dialog.close(
                rx.flex(
                    rx.button("Zapisz", on_click=LocationDialogState.update_location_name),
                    rx.button("Anuluj"),
                    spacing="2",
                    margin_top='1em'
                )
            ),
            on_close_auto_focus=AdminState.init_state
        ),
    ),


def create_location_dialog(room: RoomDto):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Dodaj nowe miejsce", on_click=LocationDialogState.init_state(None, room))),
        rx.dialog.content(
            rx.dialog.title("Dodaj nowe miejsce"),
            rx.dialog.description(
                rx.input(
                    placeholder="Podaj nazwę miejsca",
                    on_change=LocationDialogState.set_location_name,
                    value=LocationDialogState.location.name
                ),
            ),
            rx.dialog.close(
                rx.flex(
                    rx.button("Zapisz", on_click=LocationDialogState.create_new_location),
                    rx.button("Anuluj"),
                    spacing="2",
                    margin_top='1em'
                )
            ),
            on_close_auto_focus=AdminState.init_state
        ),
    ),

def delete_location_dialog(location_id):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon("octagon-x"), on_click=LocationDialogState.init_state(location_id, None))),
        rx.dialog.content(
            rx.dialog.title("Czy na pewno chcesz usunąć to miejsce?"),
            rx.dialog.close(
                rx.flex(
                    rx.button("Tak", on_click=LocationDialogState.remove_location),
                    rx.button("Nie"),
                    spacing="2",
                    margin_top='1em'
                )
            ),
            on_close_auto_focus=AdminState.init_state()
        ),
    ),