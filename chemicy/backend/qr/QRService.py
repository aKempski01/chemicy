from chemicy.backend.qr.QREnum import QREnum
from chemicy.backend.qr.QRModel import QRCodeResponseModel, QRModel
from qrcode.image.pil import PilImage
import qrcode
from io import BytesIO
import base64

from chemicy.backend.user.UserApiModel import UserLogin


def generate_qr_from_id(element_id: int, qr_type: QREnum) -> QRCodeResponseModel:
    qr_json = QRModel(id=element_id, type=qr_type)
    img: PilImage = qrcode.make(qr_json.model_dump_json())
    with BytesIO() as output:
        img.save(output, format="PNG")
        output.seek(0)
        contents = base64.b64encode(output.read())
    return QRCodeResponseModel(id=element_id, qr_code=contents)

def generate_qr_code_for_user(id_user: int, username: str, password: str) -> QRCodeResponseModel:
    qr_json = UserLogin(username=username, password=password)
    img: PilImage = qrcode.make(qr_json.model_dump_json())
    with BytesIO() as output:
        img.save(output, format="PNG")
        output.seek(0)
        contents = base64.b64encode(output.read())
    return QRCodeResponseModel(id=id_user, qr_code=contents)
