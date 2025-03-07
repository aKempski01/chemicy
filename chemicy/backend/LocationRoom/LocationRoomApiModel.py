from typing import List, Optional
from pydantic import BaseModel
from chemicy.backend.department.DepartmentDto import DepartmentApiModel

class RoomApiModel(BaseModel):
    id: int = 1
    number: str = ""
    department_id: int = 1
    department: Optional[DepartmentApiModel] = None
    qr_code: Optional[str] = None

class LocationApiModel(BaseModel):
    id: int = 1
    name: str = ""
    description: str = ""
    room_id: int = 1
    room: Optional[RoomApiModel] = None
    qr_code: Optional[str] = None

class RoomAddApiModel(BaseModel):
    id_room: int = 1

class LocationAddApiModel(BaseModel):
    id_location: int = 1
    id_room: int = 1
