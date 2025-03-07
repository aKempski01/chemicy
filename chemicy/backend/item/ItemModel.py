from typing import Optional, List
import reflex as rx
import sqlmodel
import sqlalchemy
import datetime

# class ItemModel(rx.Model, table=True):
#     item_name: str


class ItemModel(rx.Model, table=True):
    __tablename__ = "item"
    name: str
    cas: str

    amount: Optional[str]
    producent: Optional[str]



    exp_date: Optional[datetime.datetime] = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "exp_date",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )

    classification_id: Optional[int] = sqlmodel.Field(foreign_key="classification.id")
    classification: Optional["ClassificationModel"] = sqlmodel.Relationship(back_populates="item")

    status_id: int = sqlmodel.Field(foreign_key="item_status.id")
    status: Optional["ItemStatusModel"] = sqlmodel.Relationship(back_populates="item")

    user_id: int = sqlmodel.Field(foreign_key="user.id")
    user: Optional["UserModel"] = sqlmodel.Relationship(back_populates="item")

    location_id: int = sqlmodel.Field(foreign_key="location.id")
    location: Optional["LocationModel"] = sqlmodel.Relationship(back_populates="location")
