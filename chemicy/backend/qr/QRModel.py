from pydantic import BaseModel

from chemicy.backend.qr.QREnum import QREnum


class QRModel(BaseModel):
    id: int = 1
    type: QREnum = QREnum.ITEM

class QRCodeResponseModel(BaseModel):
    id: int = 1
    qr_code: str = "qr_code"