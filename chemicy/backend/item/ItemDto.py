from typing import List, Optional
from enum import Enum

import reflex as rx
from pydantic import BaseModel
from datetime import datetime

from chemicy.backend.LocationRoom.LocationRoomDto import LocationDto, RoomDto
from chemicy.backend.item_type.ItemTypeApiModel import ItemTypeApiModel
from chemicy.backend.user.UserApiModel import UserApiModel


class ItemDto(rx.base.Base):
    id: int = -1
    name: str = ""
    description: str = ""
    amount: str = ""
    producent: str = ""
    owner_id: int = -1
    owner_name: str = ""
    cas: str = ""

    p_codes: List[str] = []
    h_codes: List[str] = []

    pictogram_paths: List[str] = []

    location: LocationDto = LocationDto()
    # room: RoomDto = RoomDto()

    # Ordered   Delivered   Opened   Disposed   Missing   LowLevel
    status: str = ""