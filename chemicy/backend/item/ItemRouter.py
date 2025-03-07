from datetime import datetime

from fastapi.security import HTTPAuthorizationCredentials
from fastapi import HTTPException, Security

from chemicy.backend.LocationRoom.LocationRoomApiModel import LocationApiModel, RoomApiModel
from chemicy.backend.auth.AuthServices import verify_token, oauth2_scheme
from chemicy.backend.department.DepartmentDto import DepartmentApiModel
from chemicy.backend.faculty.FacultyApiModel import FacultyApiModel
from chemicy.backend.item.ItemApiModel import ItemApiModel, ItemStatus, ItemDetailedApiModel, \
    ItemUserAssignApiInputModel, \
    ItemReturnApiInputModel, ItemMissingApiInputModel, ItemChangeLocationApiInputModel
from typing import List

from chemicy.backend.item_type.ItemTypeApiModel import ItemTypeApiModel
from chemicy.backend.qr.QREnum import QREnum
from chemicy.backend.qr.QRModel import QRCodeResponseModel
from chemicy.backend.qr.QRService import generate_qr_from_id
from chemicy.backend.user.UserApiModel import UserApiModel


async def get_items_for_user(authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> List[ItemApiModel]:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    items: List[ItemApiModel] = []
    items.append(ItemApiModel(
        id=1,
        name="odczynnik1",
        user_id=1,
        location_id=1,
        current_user=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Ordered,

    ))
    items.append(ItemApiModel(
        id=1,
        name="odczynnik2",
        user_id=1,
        location_id=1,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Empty,

    ))
    if token_model.username:
        return items
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_item_detailed(item_id: int, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> ItemDetailedApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    item: ItemDetailedApiModel = ItemDetailedApiModel(
        id=item_id,
        name=f"odczynnik{item_id}",
        user_id=1,
        user=UserApiModel(
            id=1,
            username=token_model.username,
            name="Jan",
            surname="Kowalski",
            title="dr",
            email="jan.kowalski@polsl.pl"
        ),
        location_id=1,
        current_user_id=1,
        current_user=UserApiModel(
            id=1,
            username=token_model.username,
            name="Jan",
            surname="Kowalski",
            title="dr",
            email="jan.kowalski@polsl.pl"
        ),
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Empty,
        location=LocationApiModel(
            id=1,
            name="polka1",
            description="polka pod oknem",
            room_id=1,
            room=RoomApiModel(
                id=1,
                number="203b",
                department_id=1,
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
    )
    if token_model.username:
        return item
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_item_qr_by_id(item_id: int, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> QRCodeResponseModel:

    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    qr_response: QRCodeResponseModel = generate_qr_from_id(item_id, qr_type=QREnum.ITEM)
    if token_model.username:
        return qr_response
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def assign_to_user(data: ItemUserAssignApiInputModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> ItemDetailedApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    item: ItemDetailedApiModel = ItemDetailedApiModel(
        id=data.id_item,
        name=f"odczynnik{data.id_item}",
        user_id=1,
        location_id=1,
        current_user_id=token_model.id_user,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Empty,
    )
    if token_model.username:
        return item
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def return_to_owner(data: ItemReturnApiInputModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> ItemDetailedApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    item: ItemDetailedApiModel = ItemDetailedApiModel(
        id=data.id_item,
        name=f"odczynnik{data.id_item}",
        user_id=1,
        location_id=1,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Empty,
    )
    if token_model.username:
        return item
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def change_location(data: ItemChangeLocationApiInputModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> ItemDetailedApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    item: ItemDetailedApiModel = ItemDetailedApiModel(
        id=data.id_item,
        name=f"odczynnik{data.id_item}",
        user_id=1,
        location_id=data.id_location,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Empty,
    )
    if token_model.username:
        return item
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_items_per_location(location_id: int, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> List[ItemDetailedApiModel]:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    items: List[ItemDetailedApiModel] = []
    if location_id == 1:
        items.append(ItemDetailedApiModel(
        id=1,
        name="odczynnik1",
        user_id=1,
        location_id=1,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        location=LocationApiModel(
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
            )),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Empty,
    ))
    elif location_id == 2:
        items.append(ItemDetailedApiModel(
            id=2,
            name="odczynnik2",
            user_id=2,
            location_id=2,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
    elif location_id == 3:
        items.append(ItemDetailedApiModel(
            id=3,
            name="odczynnik3",
            user_id=2,
            location_id=3,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
    elif location_id == 4:
        items.append(ItemDetailedApiModel(
            id=4,
            name="odczynnik4",
            user_id=1,
            location_id=4,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
    elif location_id == 5:
        items.append(ItemDetailedApiModel(
            id=5,
            name="odczynnik5",
            user_id=1,
            location_id=5,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
    elif location_id == 6:
        items.append(ItemDetailedApiModel(
            id=6,
            name="odczynnik6",
            user_id=2,
            location_id=6,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
    if token_model.username:
        return items
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_items_per_room(room_id: int, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> List[ItemDetailedApiModel]:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    items: List[ItemDetailedApiModel] = []
    if room_id == 1:
        items.append(ItemDetailedApiModel(
        id=1,
        name="odczynnik1",
        user_id=1,
        location_id=1,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        location=LocationApiModel(
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
            )),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Empty,
    ))
        items.append(ItemDetailedApiModel(
            id=2,
            name="odczynnik2",
            user_id=2,
            location_id=2,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
        items.append(ItemDetailedApiModel(
            id=3,
            name="odczynnik3",
            user_id=2,
            location_id=3,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
    elif room_id == 2:
        items.append(ItemDetailedApiModel(
            id=4,
            name="odczynnik4",
            user_id=1,
            location_id=4,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
        items.append(ItemDetailedApiModel(
            id=5,
            name="odczynnik5",
            user_id=1,
            location_id=5,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
    elif room_id == 3:
        items.append(ItemDetailedApiModel(
            id=6,
            name="odczynnik6",
            user_id=2,
            location_id=6,
            current_user_id=1,
            termin_waz=datetime.now(),
            item_type_id=1,
            item_type=ItemTypeApiModel(
                id=1,
                cas_number="69-420"
            ),
            location=LocationApiModel(
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
            )),
            p_codes=["p201", "p123"],
            h_codes=["h201", "h123"],
            status=ItemStatus.Empty,
        ))
    if token_model.username:
        return items
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def dispose_of_item(data: ItemReturnApiInputModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> ItemDetailedApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    item: ItemDetailedApiModel = ItemDetailedApiModel(
        id=data.id_item,
        name=f"odczynnik{data.id_item}",
        user_id=1,
        location_id=1,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Disposed,
    )
    if token_model.username:
        return item
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def mark_missing(data: ItemMissingApiInputModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> ItemDetailedApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    item: ItemDetailedApiModel = ItemDetailedApiModel(
        id=data.id_item,
        name=f"odczynnik{data.id_item}",
        user_id=1,
        location_id=1,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Missing,
    )
    if token_model.username:
        return item
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def mark_low_level(data: ItemReturnApiInputModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> ItemDetailedApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    item: ItemDetailedApiModel = ItemDetailedApiModel(
        id=data.id_item,
        name=f"odczynnik{data.id_item}",
        user_id=1,
        location_id=1,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.LowLevel,
    )
    if token_model.username:
        return item
    raise HTTPException(status_code=401, detail="Invalid or expired token")

async def mark_empty(data: ItemReturnApiInputModel, authorization_header: HTTPAuthorizationCredentials = Security(oauth2_scheme)) -> ItemDetailedApiModel:
    """JWT-secured route with Bearer token."""
    token = authorization_header.credentials
    token_model = verify_token(token)
    item: ItemDetailedApiModel = ItemDetailedApiModel(
        id=data.id_item,
        name=f"odczynnik{data.id_item}",
        user_id=1,
        location_id=1,
        current_user_id=1,
        termin_waz=datetime.now(),
        item_type_id=1,
        item_type=ItemTypeApiModel(
            id=1,
            cas_number="69-420"
        ),
        p_codes=["p201", "p123"],
        h_codes=["h201", "h123"],
        status=ItemStatus.Empty,
    )
    if token_model.username:
        return item
    raise HTTPException(status_code=401, detail="Invalid or expired token")