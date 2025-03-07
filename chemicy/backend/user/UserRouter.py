from typing import List

from chemicy.backend.department.DepartmentDto import DepartmentApiModel
from chemicy.backend.faculty.FacultyApiModel import FacultyApiModel
from chemicy.backend.qr.QRModel import QRCodeResponseModel
from chemicy.backend.qr.QRService import generate_qr_code_for_user
from chemicy.backend.user.UserApiModel import UserQRLogin, UserLogin, UserApiModel
from chemicy.backend.auth.AuthModel import TokenResponse
from chemicy.backend.auth.AuthServices import create_token, verify_token, oauth2_scheme
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials


async def login(data: UserLogin):
    """Authenticate user using QR code and return JWT token."""
    if data.username == "admin" and data.password=="password":  # Replace with actual validation logic
        token = create_token(data.username, 1)  # Or use some dynamic username based on QR code
        return TokenResponse(jwt_token=token)
    raise HTTPException(status_code=401, detail="Invalid QR code")

async def verify_login(authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)):
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    username = token_model.username
    if username:
        return {"message": f"Hello, {username}!"}
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def generate_qr_code(authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> QRCodeResponseModel:
    """Authenticate user using QR code and return JWT token."""
    password:str = "password" #get pass from db
    token = authorization_header.credentials
    token_model = verify_token(token)
    if token_model.username:
        return generate_qr_code_for_user(token_model.id_user, token_model.username, password)
    raise HTTPException(status_code=401, detail="Invalid or expired token")


async def get_users(authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> List[UserApiModel]:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    username = token_model.username
    users: List[UserApiModel] = []
    users.append(UserApiModel(
        id=1,
        username="admin",
        name="Jan",
        surname="Kowalski",
        title="dr",
        email="jan.kowalski@polsl.pl",
        department=DepartmentApiModel(
            id=1,
            id_faculty=1,
            name="Department of Chemical Chemistry",
            description="Chemical Chemistry on Chemical Chemistry",
            faculty=FacultyApiModel(
                id=1,
                name="Faculty of Chemistry",
                description="The most Chemical faculty on SUT",
            )
        )
    ))
    users.append(UserApiModel(
        id=2,
        username="maria-curie",
        name="Maria",
        surname="Curie",
        title="prof",
        email="maria.curie@polsl.pl",
        department=DepartmentApiModel(
            id=2,
            id_faculty=1,
            name="Department of Physical Chemistry",
            description="Physical Chemistry on Chemical Physics",
            faculty=FacultyApiModel(
                id=1,
                name="Faculty of Chemistry",
                description="The most Chemical faculty on SUT",
            )
        )
    ))
    if username:
        return users
    raise HTTPException(status_code=401, detail="Invalid or expired token")