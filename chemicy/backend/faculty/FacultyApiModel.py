from pydantic import BaseModel

class FacultyApiModel(BaseModel):
    id: int = 1
    name: str = ""
    description: str = ""