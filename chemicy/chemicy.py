"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from chemicy.backend.LocationRoom.LocationRoomApiModel import LocationApiModel
from chemicy.backend.LocationRoom.LocationRoomRouter import add_room, RoomApiModel, add_location, get_rooms, \
    get_locations, get_locations_per_room, get_room_qr_by_id, get_location_qr_by_id
from chemicy.backend.auth.AuthModel import SECURITY_NEGATIVE_RESPONSES
from chemicy.backend.item.ItemApiModel import ItemDetailedApiModel, ItemReturnApiInputModel
from chemicy.backend.label.LabelApiModel import LabelApiResponse
from chemicy.backend.label.LabelRouter import generate_label
from chemicy.backend.qr.QRModel import QRCodeResponseModel
from rxconfig import config

from chemicy.main.main_page import main_page
from chemicy.search.search_page import search_page
from chemicy.register.register_page import register_page
from chemicy.admin.admin_page import admin_page
from chemicy.backend.item.ItemModel import ItemModel
from chemicy.backend.item.ItemStatusModel import ItemStatusModel
from chemicy.backend.classification.ClasifficationModel import *
from chemicy.backend.classification.PH_CodeModel import *
from chemicy.backend.user.UserModel import UserModel
from chemicy.backend.user.UserStatusModel import UserStatusModel
from chemicy.backend.user.UserRightsModel import UserrightsModel
from chemicy.backend.LocationRoom.LocationRoomModel import LocationModel, RoomModel
from chemicy.backend.department.DepartmentModel import DepartmentModel, UserDepartmentModel
from chemicy.backend.faculty.FacultyModel import FacultyModel

from chemicy.backend.user.UserRouter import TokenResponse, login, verify_login, get_users, UserApiModel, \
    generate_qr_code
from chemicy.backend.item.ItemRouter import get_items_for_user, ItemApiModel, get_item_detailed, assign_to_user, \
    return_to_owner, change_location, get_items_per_room, get_items_per_location, dispose_of_item, mark_missing, \
    mark_low_level, mark_empty, get_item_qr_by_id
from typing import List

app = rx.App()


app.api.post("/user/login", response_model=TokenResponse, responses=SECURITY_NEGATIVE_RESPONSES)(login)
app.api.get("/user/verify_login", responses=SECURITY_NEGATIVE_RESPONSES)(verify_login)
app.api.get("/user/qr", response_model=QRCodeResponseModel, responses=SECURITY_NEGATIVE_RESPONSES)(generate_qr_code)
app.api.get("/item/get_items_for_user", response_model=List[ItemApiModel], responses=SECURITY_NEGATIVE_RESPONSES)(get_items_for_user)
app.api.get("/item/get_item_detailed/{item_id}", response_model=ItemDetailedApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(get_item_detailed)
app.api.get("/item/qr/{item_id}", response_model=QRCodeResponseModel, responses=SECURITY_NEGATIVE_RESPONSES)(get_item_qr_by_id)
app.api.post("/label/generate_label", response_model=LabelApiResponse, responses=SECURITY_NEGATIVE_RESPONSES)(generate_label)
app.api.get("/user/get_users", response_model=List[UserApiModel], responses=SECURITY_NEGATIVE_RESPONSES)(get_users)
app.api.post("/item/assign_to_user", response_model=ItemDetailedApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(assign_to_user)
app.api.post("/item/return_to_owner", response_model=ItemDetailedApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(return_to_owner)
app.api.post("/item/change_location", response_model=ItemDetailedApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(change_location)

app.api.post("/room/add_room", response_model=RoomApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(add_room)
app.api.get("/room/qr/{room_id}", response_model=QRCodeResponseModel, responses=SECURITY_NEGATIVE_RESPONSES)(get_room_qr_by_id)
app.api.post("/location/add_location", response_model=LocationApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(add_location)
app.api.get("/room/get_rooms", response_model=List[RoomApiModel], responses=SECURITY_NEGATIVE_RESPONSES)(get_rooms)
app.api.get("/location/get_locations", response_model=List[LocationApiModel], responses=SECURITY_NEGATIVE_RESPONSES)(get_locations)
app.api.get("/location/qr/{location_id}", response_model=QRCodeResponseModel, responses=SECURITY_NEGATIVE_RESPONSES)(get_location_qr_by_id)
app.api.get("/location/room/{room_id}", response_model=List[LocationApiModel], responses=SECURITY_NEGATIVE_RESPONSES)(get_locations_per_room)

app.api.get("/item/room/{room_id}", response_model=List[ItemDetailedApiModel], responses=SECURITY_NEGATIVE_RESPONSES)(get_items_per_room)
app.api.get("/item/location/{location_id}", response_model=List[ItemDetailedApiModel], responses=SECURITY_NEGATIVE_RESPONSES)(get_items_per_location)

app.api.post("/item/dispose_of_item", response_model=ItemDetailedApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(dispose_of_item)
app.api.post("/item/mark_missing", response_model=ItemDetailedApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(mark_missing)
app.api.post("/item/mark_low_level", response_model=ItemDetailedApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(mark_low_level)
app.api.post("/item/mark_empty", response_model=ItemDetailedApiModel, responses=SECURITY_NEGATIVE_RESPONSES)(mark_empty)



app.add_page(main_page, route="/")
app.add_page(search_page)
app.add_page(register_page)
app.add_page(admin_page)
# app.add_page(login_page, route="/login")

