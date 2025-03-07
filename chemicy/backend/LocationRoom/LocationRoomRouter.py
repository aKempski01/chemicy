from datetime import datetime

from fastapi.security import HTTPAuthorizationCredentials
from fastapi import HTTPException, Security
from sqlalchemy.sql.functions import current_user

from chemicy.backend.LocationRoom.LocationRoomApiModel import LocationApiModel, RoomApiModel, RoomAddApiModel, \
    LocationAddApiModel
from chemicy.backend.auth.AuthServices import verify_token, oauth2_scheme
from chemicy.backend.department.DepartmentDto import DepartmentApiModel
from chemicy.backend.faculty.FacultyApiModel import FacultyApiModel
from typing import List

from chemicy.backend.qr.QREnum import QREnum
from chemicy.backend.qr.QRModel import QRCodeResponseModel
from chemicy.backend.qr.QRService import generate_qr_from_id


async def add_room(data: RoomAddApiModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> RoomApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    room: RoomApiModel = RoomApiModel(
                id=data.id_room,
                number="203b",
                department_id=1,
                qr_code=generate_qr_from_id(element_id=data.id_room, qr_type=QREnum.ROOM).qr_code,
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
            )
    if token_model.username:
        return room
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def add_location(data: LocationAddApiModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> LocationApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    room: LocationApiModel = LocationApiModel(
        id=data.id_location,
        name="polka1",
        description="polka pod oknem",
        room_id=data.id_room,
        qr_code=generate_qr_from_id(element_id=data.id_location, qr_type=QREnum.LOCATION).qr_code,
        room=RoomApiModel(
            id=data.id_room,
            number="203b",
            department_id=1,
            qr_code=generate_qr_from_id(element_id=data.id_room, qr_type=QREnum.ROOM).qr_code,
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
        )
    )
    if token_model.username:
        return room
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_rooms(authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> List[RoomApiModel]:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    rooms: List[RoomApiModel] = []
    rooms.append(RoomApiModel(
                id=1,
                number="203b",
                department_id=1,
                qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.ROOM).qr_code,
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
    rooms.append(RoomApiModel(
        id=2,
        number="204b",
        department_id=1,
        qr_code=generate_qr_from_id(element_id=2, qr_type=QREnum.ROOM).qr_code,
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
    rooms.append(RoomApiModel(
        id=3,
        number="203a",
        department_id=2,
        qr_code=generate_qr_from_id(element_id=3, qr_type=QREnum.ROOM).qr_code,
        department=DepartmentApiModel(
            id=2,
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
    if token_model.username:
        return rooms
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_locations(authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> List[LocationApiModel]:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    locations: List[LocationApiModel] = []
    locations.append(LocationApiModel(
        id=1,
        name="polka1",
        description="polka pod oknem",
        room_id=1,
        qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.LOCATION).qr_code,
        room=RoomApiModel(
            id=1,
            number="203b",
            department_id=1,
            qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.ROOM).qr_code,
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
        )))
    locations.append(LocationApiModel(
        id=2,
        name="polka2",
        description="polka pod oknem 2 ",
        room_id=1,
        qr_code=generate_qr_from_id(element_id=2, qr_type=QREnum.LOCATION).qr_code,
        room=RoomApiModel(
            id=1,
            number="203b",
            department_id=1,
            qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.ROOM).qr_code,
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
        )))
    locations.append(LocationApiModel(
        id=3,
        name="polka3",
        description="polka pod oknem3",
        room_id=1,
        qr_code=generate_qr_from_id(element_id=3, qr_type=QREnum.LOCATION).qr_code,
        room=RoomApiModel(
            id=1,
            number="203b",
            department_id=1,
            qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.ROOM).qr_code,
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
        )))
    locations.append(LocationApiModel(
        id=4,
        name="polka4",
        description="polka pod oknem 4",
        room_id=2,
        qr_code=generate_qr_from_id(element_id=4, qr_type=QREnum.LOCATION).qr_code,
        room=RoomApiModel(
            id=2,
            number="204b",
            department_id=1,
            qr_code=generate_qr_from_id(element_id=2, qr_type=QREnum.ROOM).qr_code,
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
        )))
    locations.append(LocationApiModel(
        id=5,
        name="polka5",
        description="polka pod oknem5",
        room_id=2,
        qr_code=generate_qr_from_id(element_id=5, qr_type=QREnum.LOCATION).qr_code,
        room=RoomApiModel(
            id=2,
            number="204b",
            department_id=1,
            qr_code=generate_qr_from_id(element_id=2, qr_type=QREnum.ROOM).qr_code,
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
        )))
    locations.append(LocationApiModel(
        id=6,
        name="polka6",
        description="polka pod oknem6",
        room_id=3,
        qr_code=generate_qr_from_id(element_id=6, qr_type=QREnum.LOCATION).qr_code,
        room=RoomApiModel(
            id=3,
            number="203a",
            department_id=2,
            qr_code=generate_qr_from_id(element_id=3, qr_type=QREnum.ROOM).qr_code,
            department=DepartmentApiModel(
                id=2,
                id_faculty=1,
                name="Department of Chemical Chemistry",
                description="Chemical Chemistry on Chemical Chemistry",
                faculty=FacultyApiModel(
                    id=1,
                    name="Faculty of Chemistry",
                    description="The most Chemical faculty on SUT",
                )
            )
        )))
    if token_model.username:
        return locations
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_locations_per_room(room_id: int, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> List[LocationApiModel]:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    locations: List[LocationApiModel] = []
    if room_id == 1:
        locations.append(LocationApiModel(
            id=1,
            name="polka1",
            description="polka pod oknem",
            room_id=1,
            qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.LOCATION).qr_code,
            room=RoomApiModel(
                id=1,
                number="203b",
                department_id=1,
                qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.ROOM).qr_code,
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
            )))
        locations.append(LocationApiModel(
            id=2,
            name="polka2",
            description="polka pod oknem 2 ",
            room_id=1,
            qr_code=generate_qr_from_id(element_id=2, qr_type=QREnum.LOCATION).qr_code,
            room=RoomApiModel(
                id=1,
                number="203b",
                department_id=1,
                qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.ROOM).qr_code,
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
            )))
        locations.append(LocationApiModel(
            id=3,
            name="polka3",
            description="polka pod oknem3",
            room_id=1,
            qr_code=generate_qr_from_id(element_id=3, qr_type=QREnum.LOCATION).qr_code,
            room=RoomApiModel(
                id=1,
                number="203b",
                department_id=1,
                qr_code=generate_qr_from_id(element_id=1, qr_type=QREnum.ROOM).qr_code,
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
            )))
    elif room_id == 2:
        locations.append(LocationApiModel(
            id=4,
            name="polka4",
            description="polka pod oknem 4",
            room_id=2,
            qr_code=generate_qr_from_id(element_id=4, qr_type=QREnum.LOCATION).qr_code,
            room=RoomApiModel(
                id=2,
                number="204b",
                department_id=1,
                qr_code=generate_qr_from_id(element_id=2, qr_type=QREnum.ROOM).qr_code,
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
            )))
        locations.append(LocationApiModel(
            id=5,
            name="polka5",
            description="polka pod oknem5",
            room_id=2,
            qr_code=generate_qr_from_id(element_id=5, qr_type=QREnum.LOCATION).qr_code,
            room=RoomApiModel(
                id=2,
                number="204b",
                department_id=1,
                qr_code=generate_qr_from_id(element_id=2, qr_type=QREnum.ROOM).qr_code,
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
            )))

    elif room_id==3:
        locations.append(LocationApiModel(
            id=6,
            name="polka6",
            description="polka pod oknem6",
            room_id=3,
            qr_code=generate_qr_from_id(element_id=6, qr_type=QREnum.LOCATION).qr_code,
            room=RoomApiModel(
                id=3,
                number="203a",
                department_id=2,
                qr_code=generate_qr_from_id(element_id=3, qr_type=QREnum.ROOM).qr_code,
                department=DepartmentApiModel(
                    id=2,
                    id_faculty=1,
                    name="Department of Chemical Chemistry",
                    description="Chemical Chemistry on Chemical Chemistry",
                    faculty=FacultyApiModel(
                        id=1,
                        name="Faculty of Chemistry",
                        description="The most Chemical faculty on SUT",
                    )
                )
            )))
    if token_model.username:
        return locations
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_room_qr_by_id(room_id: int, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> QRCodeResponseModel:
    """Authenticate user using QR code and return JWT token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    if token_model.username:
        return generate_qr_from_id(room_id, QREnum.ROOM)
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_location_qr_by_id(location_id: int, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> QRCodeResponseModel:
    """Authenticate user using QR code and return JWT token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    if token_model.username:
        return generate_qr_from_id(location_id, QREnum.LOCATION)
    raise HTTPException(status_code=401, detail="Invalid or expired token")