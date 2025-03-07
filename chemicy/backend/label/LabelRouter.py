from fastapi.security import HTTPAuthorizationCredentials
from fastapi import HTTPException, Security
from chemicy.backend.auth.AuthServices import verify_token, oauth2_scheme
from chemicy.backend.label.LabelApiModel import LabelApiBody, LabelApiResponse


async def generate_label(data: LabelApiBody, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> LabelApiResponse:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    username = token_model.username
    items = []
    for id in data.id_item:
        items.append("UklGRmwAAABXRUJQVlA4IGAAAAAwBACdASoYABgAP3GuzV+0rSilqAgCkC4JQBmDgsiSpIv92vkkXrAtc0AA/t/8oKpLNnWeC8WeIKaXY//9K5wyClBUuBipO4IHUxFJDApoaH64tJuHJDT40v3ojwAAAAA=")
    label: LabelApiResponse =  LabelApiResponse(
        label=items
    )
    if username:
        return label
    raise HTTPException(status_code=401, detail="Invalid or expired token")
