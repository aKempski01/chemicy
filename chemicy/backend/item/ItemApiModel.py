from pydantic import BaseModel

from chemicy.backend.LocationRoom.LocationRoomApiModel import LocationApiModel
from chemicy.backend.item.ItemEnum import ItemStatus
from datetime import datetime
from typing import Optional, List

from chemicy.backend.item_type.ItemTypeApiModel import ItemTypeApiModel
from chemicy.backend.user.UserApiModel import UserApiModel


class ItemApiModel(BaseModel):
    id: int = 1
    name: str = ""
    user_id: int = 1
    location_id: int = 1
    current_user: int = 1
    termin_waz: datetime = datetime.now()
    item_type_id: int = 1
    p_codes: List[str] = []
    h_codes: List[str] = []

    #location: LocationDto = LocationDto()
    #room: RoomDto = RoomDto()
    status: ItemStatus = ItemStatus.Ordered

class ItemDetailedApiModel(BaseModel):
    id: int = 1
    name: str = ""
    user_id: int = 1
    user: Optional[UserApiModel] = None
    location_id: int = 1
    current_user_id: int = 1
    current_user: Optional[UserApiModel] = None
    termin_waz: datetime = datetime.now()
    item_type_id: int = 1
    item_type: Optional[ItemTypeApiModel] = None
    p_codes: List[str] = []
    h_codes: List[str] = []
    location: Optional[LocationApiModel] = None
    status: ItemStatus = ItemStatus.Ordered

class ItemUserAssignApiInputModel(BaseModel):
    id_item: int = 1

class ItemReturnApiInputModel(BaseModel):
    id_item: int = 1

class ItemMissingApiInputModel(BaseModel):
    id_item: int = 1

class ItemChangeLocationApiInputModel(BaseModel):
    id_item: int = 1
    id_location: int = 1
