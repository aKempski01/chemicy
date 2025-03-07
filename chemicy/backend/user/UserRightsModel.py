import reflex as rx
import sqlmodel

class UserrightsModel(rx.Model, table=True):
    __tablename__ = 'user_right'
    name: str
    users: list["UserModel"] = sqlmodel.Relationship(back_populates="user_right")

