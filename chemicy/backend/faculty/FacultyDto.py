from typing import List

import reflex as rx

from chemicy.backend.department.DepartmentDto import DepartmentDto


class FacultyDto(rx.base.Base):
    id: int = -1
    name: str = ""
    departments: List[DepartmentDto] = []


