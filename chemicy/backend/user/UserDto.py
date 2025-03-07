import uuid
from typing import Optional, List

import reflex as rx

from chemicy.backend.item.ItemDto import ItemDto


class UserDto(rx.base.Base):
    id: int = -1
    name: str = ""
    surname: str = ""
    password: Optional[str] = None

    email: Optional[str] = "-"
    phone: Optional[str] = "-"
    office_room: Optional[str] = "-"
    website: Optional[str] = "-"

    department: str = ""
    faculty: str = ""

    items: List[ItemDto] = []

    "Pending Suspended Archived Active"
    status: str = "Pending"

    "None Admin SuperAdmin"
    rights: str = "None"
