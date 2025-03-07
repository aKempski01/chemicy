from typing import List

import reflex as rx
import sqlmodel


class FacultyModel(rx.Model, table = True):
    __tablename__ = 'faculty'
    name: str
    description: str

    deparments: List["DepartmentModel"] = sqlmodel.Relationship(back_populates="faculty")