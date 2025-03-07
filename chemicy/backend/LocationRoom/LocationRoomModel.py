from typing import Optional, List

import reflex as rx
import sqlmodel


class LocationModel(rx.Model, table=True):
    __tablename__ = 'location'
    name: str

    users: List["UserModel"] = sqlmodel.Relationship(back_populates="location")
    items: List["ItemModel"] = sqlmodel.Relationship(back_populates="location")

    room_id: int = sqlmodel.Field(foreign_key="room.id")
    room: Optional["RoomModel"] = sqlmodel.Relationship(back_populates="location")



class RoomModel(rx.Model, table=True):
    __tablename__ = 'room'
    name: str

    locations: List["LocationModel"] = sqlmodel.Relationship(back_populates="room")

    department_id: int = sqlmodel.Field(foreign_key="department.id")
    department: Optional["DepartmentModel"] = sqlmodel.Relationship(back_populates="room")
