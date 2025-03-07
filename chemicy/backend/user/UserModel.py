from typing import Optional, List

import reflex as rx
import sqlmodel


class UserModel(rx.Model, table=True):
    __tablename__ = 'user'
    name: str
    surname: str

    email: str
    password: str
    
    office_room: str
    telephone_number: str
    website: str

    items: List["ItemModel"] = sqlmodel.Relationship(back_populates="user")
    user_departments: List["UserDepartmentModel"] = sqlmodel.Relationship(back_populates="user")

    status_id: int = sqlmodel.Field(foreign_key="user_status.id")
    status: Optional["UserStatusModel"] = sqlmodel.Relationship(back_populates="user")

    right_id: int = sqlmodel.Field(foreign_key="user_right.id")
    right: Optional["UserRightModel"] = sqlmodel.Relationship(back_populates="user")
