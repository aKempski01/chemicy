from typing import List, Optional
import reflex as rx
import sqlalchemy

from chemicy.backend.LocationRoom.LocationRoomDto import RoomDto, LocationDto, LocationNoRefDto


def get_rooms_db() -> List[RoomDto]:
    rooms = []
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT r.id, r.name "
                "FROM room r "
            ),
        )
        for r in res:

            locs = get_locations_no_reference_for_room_id(r[0])
            room = RoomDto(id=r[0], name=r[1], locations=locs)
            rooms.append(room)

    return rooms


def get_locations_no_reference_for_room_id(room_id: int) -> List[LocationNoRefDto]:
    locations = []
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT l.id, l.name "
                "FROM location l "
                "WHERE l.room_id = (:room_id)",
            ),{"room_id": room_id}
        )

        for r in res:
            location = LocationNoRefDto(id=r[0], name=r[1])
            locations.append(location)
    return locations

def get_location_by_id(location_id: int) -> Optional[LocationDto]:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT l.id, l.name "
                "FROM location l "
                "WHERE l.id = (:id)",
            ),{"id": location_id}
        )
    for r in res:
        location = LocationDto(id=r[0], name=r[1])
        return location

    return None



def update_location_name(location: LocationDto) -> LocationDto:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "UPDATE location "
                "SET name = (:name) "
                "WHERE id = (:id)",
            ),{"id": location.id, "name": location.name}
        )
        session.commit()

def delete_location(location: LocationDto) -> None:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "DELETE FROM location WHERE id = (:id)",
            ), {"id": location.id}
        )
        session.commit()

def create_location(location: LocationDto) -> LocationDto:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "INSERT INTO location (name, room_id) "
                "VALUES (:name, :room_id)",
            ), {"name": location.name, "room_id": location.room.id}
        )
        session.commit()

def get_rooms() -> List[RoomDto]:
    r1 = RoomDto(id = 0, name='301')
    r2 = RoomDto(id = 1, name='302')
    r3 = RoomDto(id = 2, name='303')

    return [r1, r2, r3]



def get_locations_for_room_id(room_id: int) -> List[LocationDto]:
    r1 = RoomDto(id = 0, name='301')
    l1 = LocationDto(id = 0, name='shelf 1', room=r1)
    l1_2 = LocationDto(id = 1, name='shelf 2', room=r1)
    l1_3 = LocationDto(id = 2, name='shelf 3', room=r1)

    r2 = RoomDto(id = 1, name='302')
    l2 = LocationDto(id = 3, name='Fridge 1', room=r2)
    l2_2 = LocationDto(id = 4, name='Fridge 2', room=r2)

    r3 = RoomDto(id = 2, name='303')
    l3 = LocationDto(id = 5, name='Desk 1', room=r3)
    l3_2 = LocationDto(id = 6, name='Desk 2', room=r3)
    l3_3 = LocationDto(id = 7, name='Shelf', room=r3)
    locations = [l1, l1_2, l1_3, l2, l2_2, l3, l3_2, l3_3]
    locations = [l for l in locations if l.room.id == room_id]
    return locations
