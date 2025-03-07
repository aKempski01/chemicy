import reflex as rx
import sqlmodel


class UserStatusModel(rx.Model, table=True):
    __tablename__ = 'user_status'
    name: str
    color: str
    users: list["UserModel"] = sqlmodel.Relationship(back_populates="user_status")

