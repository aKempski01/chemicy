from typing import Optional

from pydantic import BaseModel

from chemicy.backend.department.DepartmentDto import DepartmentApiModel


class UserLogin(BaseModel):
    username: str
    password: str

class UserQRLogin(BaseModel):
    qr_code: str

class UserApiModel(BaseModel):
    id: int = 1
    username: str = ""
    email: str = ""
    title: str = ""
    name: str = ""
    surname: str = ""
    department: Optional[DepartmentApiModel] = None

class UserTokenModel(BaseModel):
    id_user: int = 1
    username: str = ""