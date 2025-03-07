from typing import List
import reflex as rx
import sqlalchemy
from chemicy.backend.LocationRoom.LocationRoomDto import RoomDto, LocationDto
from chemicy.backend.item.ItemDto import ItemDto



def get_all_items_db() -> List[ItemDto]:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT i.id, i.name, i.amount, i.producent, i.exp_date, i.status_id, i.user_id, i.location_id, l.name, l.room_id, r.name, u.name, u.surname  "
                "FROM item i "
                "JOIN location l ON l.id == i.location_id "
                "JOIN room r on r.id == l.room_id " 
                "JOIN user u on i.user_id  == u.id"
            )
        )
    items = []

    for r in res:
        owner_name = r[-1] +" "+r[-2]
        room = RoomDto(id = r[-4], name=r[-3])
        loc = LocationDto(id = r[-6], name=r[-5], room = room)

        item = ItemDto(id=r[0], name=r[1], amount=r[2], producent=r[3], status=r[5], cas = "11-120", owner_id=r[6], owner_name=owner_name, location=loc)
        items.append(item)

    return items


def get_all_items():
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



    i1 = ItemDto(id=0, name='odczynnik 1',description='asd', location=l1, status = "OK", owner_id=0, cas = "321-77358",
                      h_codes=['H302', 'H314', 'H317'], p_codes=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
    i2 = ItemDto(id=1, name='odczynnik 2',description='asd', location=l1_2, status = "OK", owner_id=1, cas = "629-77894",
                      h_codes=['H302', 'H314', 'H317'], p_codes=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
    i3 = ItemDto(id=2, name='odczynnik 3',description='asd', location=l1_3, status = "Low Level", owner_id=0, cas = "124-73898",
                      h_codes=['H302', 'H314', 'H317'], p_codes=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
    i4 = ItemDto(id=3, name='odczynnik 4',description='asd', location=l2, status = "Delivery", owner_id=2, cas = "624-88791",
                      h_codes=['H302', 'H314', 'H317'], p_codes=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
    i5 = ItemDto(id=4, name='odczynnik 5',description='asd', location=l2_2, status = "Missing", owner_id=3, cas = "624-7238",
                      h_codes=['H302', 'H314', 'H317'], p_codes=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
    i6 = ItemDto(id=5, name='odczynnik 6',description='asd', location=l3, status = "To Buy", owner_id=5, cas = "889-73582",
                      h_codes=['H302', 'H314', 'H317'], p_codes=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])

    return [i1, i2, i3, i4, i5, i6]
