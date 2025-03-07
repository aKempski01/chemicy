from typing import Optional, List

import reflex as rx
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from chemicy.backend.item.ItemDto import ItemDto
from chemicy.backend.LocationRoom.LocationRoomDto import LocationDto, RoomDto
from chemicy.backend.user.UserDto import UserDto
from chemicy.backend.user.UserService import get_all_users
from chemicy.backend.LocationRoom.LocationRoomService import get_rooms, get_locations_for_room_id
from chemicy.session.session_state import SessionState

import glob

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# from chemicy.search_test.router import get_rooms, get_places_for_room_id

class ItemState(SessionState):
    item: Optional[ItemDto]

    owner: Optional[UserDto]
    users: List[UserDto]

    user_names: List[str]
    selected_username: str

    rooms: List[RoomDto]
    room_names: List[str]
    selected_room: str

    locations: List[LocationDto]
    location_names: List[str]
    selected_location: str

    edit_mode: bool = False
    editable: bool = False

    def load_item(self, item: ItemDto):
        self.item = item
        self.users = get_all_users()
        self.owner = [u for u in self. users if u.id == item.owner_id][0]
        self.user_names = [u.surname + "  " + u.name for u in self.users]
        self.selected_username = self.owner.surname + "  " + self.owner.name

        self.rooms = get_rooms()
        self.room_names = [r.name for r in self.rooms]
        self.selected_room = self.item.location.room.name

        self.locations = get_locations_for_room_id(item.location.room.id)
        self.location_names = [l.name for l in self.locations]
        self.selected_location = self.item.location.name

        self.edit_mode = False
        self.editable = item.owner_id == self.user.id

    @rx.event
    def print_label(self):
        im = np.ones((2790, 3960, 3), dtype=np.uint8)
        im *= 255

        cv.line(im, (0, 370), (3960, 370), (0,0,0), 2)
        cv.line(im, (2600, 370), (2600, 2790), (0,0,0), 2)



        pictograms = self.item.pictogram_paths
        for i in range(len(pictograms)):
            p = glob.glob("assets/pictograms/"+ pictograms[i] + "*")[0]
            pic = cv.imread(p)
            pic = cv.resize(pic, (300,300))

            buf_x = int(i%3)*340

            buf_y = int(i/3)*340

            im[buf_y+600: buf_y+600 + 300, buf_x+2700:buf_x+2700+300, :] = pic


        lines = []
        for i in range(len(self.item.p_codes)):
            if len(self.item.p_codes[i] + " " + self.item.p_warning_codes_pl[i]) > 70:
                idx = (self.item.p_codes[i] + " " + self.item.p_warning_codes_pl[i])[:70].rfind(" ")
                lines.append((self.item.p_codes[i] + " " + self.item.p_warning_codes_pl[i])[:idx])

                l = (self.item.p_codes[i] + " " + self.item.p_warning_codes_pl[i])[idx:]
                if len(l) > 70:
                    idx = l[:70].rfind(" ")
                    lines.append(l[:idx])
                    lines.append(l[idx:])
                else:
                    lines.append(l)

            else:
                lines.append(self.item.p_codes[i] + " " + self.item.p_warning_codes_pl[i])

            if len(self.item.p_warning_codes_en[i]) > 70:
                idx = self.item.p_warning_codes_en[i][:70].rfind(" ")
                lines.append(self.item.p_warning_codes_en[i][:idx])

                l = self.item.p_warning_codes_en[i][idx:]
                if len(l) > 70:
                    idx = l[:70].rfind(" ")
                    lines.append(l[:idx])
                    lines.append(l[idx:])
                else:
                    lines.append(l)
            else:
                lines.append(self.item.p_warning_codes_en[i])
            lines.append(" ")


        for i in range(len(self.item.h_codes)):
            if len(self.item.h_codes[i] + " " + self.item.h_warning_codes_pl[i]) > 70:
                idx = (self.item.h_codes[i] + " " + self.item.h_warning_codes_pl[i])[:70].rfind(" ")
                lines.append((self.item.h_codes[i] + " " + self.item.h_warning_codes_pl[i])[:idx])

                l = (self.item.h_codes[i] + " " + self.item.h_warning_codes_pl[i])[idx:]
                if len(l) > 70:
                    idx = l[:70].rfind(" ")
                    lines.append(l[:idx])
                    lines.append(l[idx:])

                else:
                    lines.append(l)

            else:
                lines.append(self.item.h_codes[i] + " " + self.item.h_warning_codes_pl[i])

            if len(self.item.h_warning_codes_en[i]) > 70:
                idx = self.item.h_warning_codes_en[i][:70].rfind(" ")
                lines.append(self.item.h_warning_codes_en[i][:idx])

                l = self.item.h_warning_codes_en[i][idx:]
                if len(l) > 70:
                    idx = l[:70].rfind(" ")
                    lines.append(l[:idx])
                    lines.append(l[idx:])
                else:
                    lines.append(l)
            else:
                lines.append(self.item.h_warning_codes_en[i])

            lines.append(" ")




        pil_image = Image.fromarray(im)
        font_big = ImageFont.truetype("assets/fonts/AbhayaLibre-Regular.ttf",150)
        font = ImageFont.truetype("assets/fonts/AbhayaLibre-Regular.ttf",70)
        draw = ImageDraw.Draw(pil_image)

        draw.text((10, 200), self.item.name, font=font_big, fill='black')
        draw.text((10, 400), "numer cas: " + self.item.cas, font=font_big, fill='black')
        draw.text((10, 550), "objętość: " + self.item.amount, font=font_big, fill='black')
        draw.text((2700, 400), self.item.danger_status, font=font_big, fill='black')



        for i in range(len(lines)):
            draw.text((15, 750 + i*70), lines[i], font=font, fill='black')

            # cv.putText(im, lines[i], (15, 750 + i*70), cv.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 2)
        im = np.asarray(pil_image)
        # im = cv.cvtColor(im, cv.COLOR_RGB2BGR)

        cv.imwrite('image.jpg', im)


    def update_name(self, name: str):
        self.reagent.name = name

    def update_amount(self, amount: str):
        self.reagent.amount = amount

    def update_cas(self, cas: str):
        self.reagent.cas = cas

    def update_owner(self, owner_name: str):
        idx = [i for i in range(len(self.user_names)) if self.user_names[i] == owner_name][0]
        self.owner = self.users[idx]
        self.selected_username = self.user_names[idx]

    def update_room(self, room_name: str):
        self.selected_room = room_name

        self.location_names = [l.name for l in self.locations]
        self.selected_location = self.location_names[0]

    def update_location(self, location_name: str):
        self.selected_location = location_name

    def update_producent(self, producent_name: str):
        self.item.producent = producent_name

    def edit_btn(self):
        self.edit_mode = True

