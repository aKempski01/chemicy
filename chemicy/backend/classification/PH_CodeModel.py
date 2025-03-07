from typing import Optional, List

import reflex as rx
import sqlmodel


class PH_CodeModel(rx.Model, table = True):
    __tablename__ = 'ph_code'

    code: str
    warning_text_pl: Optional[str]
    warning_text_en: Optional[str]

    id_status: Optional[int] = sqlmodel.Field(foreign_key="ph_code_status.id")
    status: Optional["PH_Code_StatusModel"] = sqlmodel.Relationship(back_populates="ph_code")



class PH_Code_StatusModel(rx.Model, table = True):
    __tablename__ = 'ph_code_status'
    status_name: str


class PH_DangerClassModel(rx.Model, table = True):
    __tablename__ = 'ph_danger_class'
    danger_class: str



class PictogramModel(rx.Model, table = True):
    __tablename__ = 'pictogram'
    path: str






class Pictogram_PH_CodeModel(rx.Model, table = True):
    __tablename__ = 'pictogram_ph_code'

    id_pictogram: Optional[int] = sqlmodel.Field(foreign_key="pictogram.id")
    pictogram: Optional["PictogramModel"] = sqlmodel.Relationship(back_populates="pictogram_ph_code")

    id_PH_Code: Optional[int] = sqlmodel.Field(foreign_key="ph_code.id")
    PH_Code: Optional["PH_CodeModel"] = sqlmodel.Relationship(back_populates="pictogram_ph_code")



class PH_CodeDangerModel(rx.Model, table = True):
    __tablename__ = 'ph_code_danger'

    id_danger_class: Optional[int] = sqlmodel.Field(foreign_key="ph_danger_class.id")
    danger_class: Optional["PictogramModel"] = sqlmodel.Relationship(back_populates="ph_code_danger")

    id_PH_Code: Optional[int] = sqlmodel.Field(foreign_key="ph_code.id")
    PH_Code: Optional["PH_DangerClassModel"] = sqlmodel.Relationship(back_populates="ph_code_danger")


