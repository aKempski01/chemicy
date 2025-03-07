from pydantic import BaseModel


class ItemTypeApiModel(BaseModel):
    id: int = 1
    cas_number: str = ""

