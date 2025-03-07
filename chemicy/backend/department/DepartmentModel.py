from typing import Optional, List

import reflex as rx
import sqlmodel


class DepartmentModel(rx.Model, table = True):
    __tablename__ = 'department'
    name: str
    description: str

    user_departments: List['UserDepartmentModel'] = sqlmodel.Relationship(back_populates="department")
    rooms: List['RoomModel'] = sqlmodel.Relationship(back_populates="department")

    faculty_id: int = sqlmodel.Field(foreign_key="faculty.id")
    faculty: Optional["FacultyModel"] = sqlmodel.Relationship(back_populates="department")


class UserDepartmentModel(rx.Model, table = True):
    __tablename__ = 'user_department'
    department_id: int = sqlmodel.Field(foreign_key="department.id")
    department: Optional["DepartmentModel"] = sqlmodel.Relationship(back_populates="user_department")

    user_id: int = sqlmodel.Field(foreign_key="user.id")
    user: Optional["UserModel"] = sqlmodel.Relationship(back_populates="user_department")
