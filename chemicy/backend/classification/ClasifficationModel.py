from typing import List, Optional

import reflex as rx
import sqlmodel


class ClassificationModel(rx.Model, table = True):
    __tablename__ = 'classification'

    items: List['ItemModel'] = sqlmodel.Relationship(back_populates="classification")
    classification_codes: List['ClassificationCodeModel'] = sqlmodel.Relationship(back_populates="classification")



class ClassificationCodeModel(rx.Model, table = True):
    __tablename__ = 'classification_code'

    id_classification: Optional[int] = sqlmodel.Field(foreign_key="classification.id")
    classification: Optional["ClassificationModel"] = sqlmodel.Relationship(back_populates="classification_code")

    id_ph_code: Optional[int] = sqlmodel.Field(foreign_key="ph_code.id")
    ph_code: Optional["PH_CodeModel"] = sqlmodel.Relationship(back_populates="classification_code")

