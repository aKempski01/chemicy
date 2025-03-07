from typing import List

from chemicy.backend.label.LabelEnum import LabelType
from pydantic import BaseModel


class LabelApiBody(BaseModel):
    type: LabelType = LabelType.QR_CODE_SPECIFICATION
    id_item: List[int]

class LabelApiResponse(BaseModel):
    label: List[str] = []
