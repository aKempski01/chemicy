import datetime
from authlib.jose.errors import DecodeError, ExpiredTokenError, InvalidClaimError
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer

from authlib.jose import jwt

from chemicy.backend.user.UserApiModel import UserTokenModel

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
oauth2_scheme = HTTPBearer()

# Create JWT token
def create_token(username: str, id_user: int) -> str:
    payload = {
        "sub": username,
        "id_user": id_user,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Expiration time
    }
    token = jwt.encode({"alg": ALGORITHM}, payload, SECRET_KEY)
    return token

def verify_token(token: str) -> UserTokenModel:
    try:
        payload = jwt.decode(token, SECRET_KEY)
        user_token = UserTokenModel(id_user=payload["id_user"], username=payload["sub"])
        return user_token
    except ExpiredTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The token has expired.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e
    except InvalidClaimError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e
    except DecodeError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e