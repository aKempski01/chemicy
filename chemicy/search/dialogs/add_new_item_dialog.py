from typing import List

import reflex as rx
from docutils.nodes import description

from chemicy.backend.LocationRoom.LocationRoomDto import RoomDto, LocationDto
from chemicy.backend.LocationRoom.LocationRoomService import get_rooms, get_locations_for_room_id
from chemicy.backend.item.ItemDto import ItemDto
from chemicy.backend.item_type.itemTypeService import validate_cas, get_p_h_codes_for_cas

class AddNewItemState(rx.State):
    item = ItemDto()

    rooms: List[RoomDto]
    room_names: List[str]
    selected_room: str
    statuses: List[str]

    locations: List[LocationDto]
    location_names: List[str]
    selected_location: str

    correct_cas: bool = False
    can_save: bool = False

    def init_state(self):
        self.item = ItemDto()

        self.rooms = get_rooms()
        self.room_names = [r.name for r in self.rooms]
        self.selected_room = self.item.location.room.name
        self.statuses = ["Ordered", "Delivered", "Opened", "Disposed", "Missing", "LowLevel"]
        self.correct_cas = False
        self.update_can_save()

    def update_can_save(self):
        if self.correct_cas and self.item.name != "" and self.item.status != "" and self.item.room.id != -1 and self.item.location.id != -1:
            self.can_save = True
        else:
            self.can_save = False

    def update_name(self, name):
        self.item.name = name
        self.update_can_save()

    def update_cas(self, cas):
        self.item.cas = cas
        if validate_cas(cas):
            self.correct_cas = True
            ph = get_p_h_codes_for_cas(cas)
            self.item.p_codes = ph['p_codes']
            self.item.h_codes = ph['h_codes']
        else:
            self.correct_cas = False
            self.item.p_codes = []
            self.item.h_codes = []

        self.update_can_save()

    def update_description(self, description):
        self.item.description = description


    def update_room(self, room_name: str):
        r = [r for r in self.rooms if r.name == room_name][0]
        self.selected_room = r.name
        # self.item.room = [r for r in self.rooms if r.name == room_name][0]
        self.locations = get_locations_for_room_id(r.id)
        self.location_names = [l.name for l in self.locations]
        self.selected_location = self.item.location.name
        self.update_can_save()

    def update_location(self, location_name: str):
        self.item.location = [l for l in self.locations if l.name == location_name][0]
        self.update_can_save()

    def update_amount(self, amount):
        self.item.amount = amount


    def update_producent(self, producent):
        self.item.producent = producent


    def update_status(self, status):
        self.item.status = status
        self.update_can_save()


def add_mew_item_dialog():
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Nowy odczynnik", on_click=AddNewItemState.init_state)),
        rx.dialog.content(
            rx.dialog.title("Dodaj nowy odczynnik"),
            rx.dialog.description(
                rx.flex(
                    rx.card(
                        rx.heading("Nazwa odczynnika"),
                        rx.input(
                            placeholder="Enter text...",
                            value=AddNewItemState.item.name,
                            on_change=AddNewItemState.update_name),
                        rx.heading("Ilość"),
                        rx.input(
                            placeholder="Enter text...",
                            value=AddNewItemState.item.amount,
                            on_change=AddNewItemState.update_amount),
                        rx.hstack(
                            rx.vstack(
                                rx.heading("Zagrożenia P", size="3"),
                                rx.list.unordered(
                                    rx.foreach(AddNewItemState.item.p_codes, lambda p: rx.list.item(p)),
                                ),
                            ),
                            rx.vstack(
                                rx.heading("Zagrożenia H", size="3"),
                                rx.list.unordered(
                                    rx.foreach(AddNewItemState.item.h_codes, lambda h: rx.list.item(h)),
                                )
                            ),
                        ),
                        width="50%",
                    ),
                    rx.card(
                        rx.heading("Numer CAS"),
                        rx.input(
                            placeholder="Enter text...",
                            value=AddNewItemState.item.cas,
                            on_change=AddNewItemState.update_cas),
                        rx.heading("Pokój"),
                        rx.select(AddNewItemState.room_names,
                                  value=AddNewItemState.item.location.room.name,
                                  on_change=AddNewItemState.update_room),
                        rx.heading("Miejsce"),
                        rx.select(AddNewItemState.location_names,
                                  value=AddNewItemState.item.location.name,
                                  on_change=AddNewItemState.update_location),
                        rx.heading("Status"),
                        rx.select(AddNewItemState.statuses,
                                  value=AddNewItemState.item.status,
                                  on_change=AddNewItemState.update_status),
                        rx.heading("Producent"),
                        rx.input(
                            placeholder="Enter text...",
                            value=AddNewItemState.item.producent,
                            on_change=AddNewItemState.update_producent),

                        width="50%",
                    ),
                    spacing="2",
                    direction="row",
                )
            ),
            rx.dialog.close(
                rx.hstack(
                    rx.button("Zapisz zmiany", size="3", disabled=~AddNewItemState.can_save),
                    rx.button("Anuluj", size="3"),
                )
            ),
        ),
    )
