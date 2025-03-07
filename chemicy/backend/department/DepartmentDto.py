from typing import Optional

import reflex as rx
from pydantic import BaseModel

from chemicy.backend.faculty.FacultyApiModel import FacultyApiModel


class DepartmentDto(rx.base.Base):
    id: int = -1
    name: str

class DepartmentApiModel(BaseModel):
    id: int = 1
    id_faculty: int = 1
    name: str
    description: str

    faculty: Optional[FacultyApiModel] = None