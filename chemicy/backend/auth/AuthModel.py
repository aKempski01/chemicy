from pydantic import BaseModel

class TokenResponse(BaseModel):
    jwt_token: str

SECURITY_NEGATIVE_RESPONSES = {
    401: {
        "description": "Unauthorized",
        "content": {"application/json": {"example": {"detail": "The token has expired."}}},
    },
    403: {
        "description": "Forbidden",
        "content": {"application/json": {"example": {"detail": "Invalid or missing authentication token"}}},
    },
    500: {
        "description": "Internal server error",
        "content": {"application/json": {"example": {"detail": "Internal server error"}}},
    },
}