import reflex as rx
import sqlmodel
import sqlalchemy


class ItemStatusModel(rx.Model, table=True):
    __tablename__ = 'item_status'
    name: str
    color: str

    items: list["ItemModel"] = sqlmodel.Relationship(back_populates="item_status")

