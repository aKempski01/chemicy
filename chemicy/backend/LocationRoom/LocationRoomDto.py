from typing import List, Optional
import reflex as rx


class LocationNoRefDto(rx.base.Base):
    id: int = -1
    name: str = ""

class RoomDto(rx.base.Base):
    id: int = -1
    name: str = ""
    locations: List[LocationNoRefDto] = []


class LocationDto(rx.base.Base):
    id: int = -1
    name: str = ""
    room: Optional[RoomDto] = None
