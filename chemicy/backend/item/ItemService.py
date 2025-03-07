from typing import List
import reflex as rx
import sqlalchemy
from chemicy.backend.LocationRoom.LocationRoomDto import RoomDto, LocationDto
from chemicy.backend.item.ItemDto import ItemDto



def get_all_items_db() -> List[ItemDto]:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT i.id, i.name, i.amount, i.producent, i.exp_date, iss.name, i.user_id, i.location_id, l.name, l.room_id, r.name, u.name, u.surname  "
                "FROM item i "
                "JOIN location l ON l.id == i.location_id "
                "JOIN room r on r.id == l.room_id " 
                "JOIN item_status iss on iss.id == i.status_id "
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

    for i in items:
        pics = []
        with rx.session() as session:
            res = session.execute(
                sqlalchemy.text("SELECT pc.code, pc.warning_text_pl, pc.warning_text_en, pcs.status_name from ph_code pc " 
                                    "join classification_code cc on cc.id_ph_code == pc.id "
                                    "join classification c ON c.id == cc.id_classification "
                                    "join item i on i.classification_id == c.id "
                                    "join ph_code_status pcs on pcs.id ==pc.id_status "
                                    "where i.id == (:i_id)"),{"i_id": i.id})

            for r in res:
                if r[0][0] != "P":
                    i.h_codes.append(r[0])
                    i.h_warning_codes_pl.append(r[1])
                    i.h_warning_codes_en.append(r[2])
                else:
                    i.p_codes.append(r[0])
                    i.p_warning_codes_pl.append(r[1])
                    i.p_warning_codes_en.append(r[2])

                if r[3] == "Niebezpieczeństwo":
                    i.danger_status = "Niebezpieczeństwo"

            res = session.execute(
                sqlalchemy.text("SELECT p.path from pictogram p " 
                                "join pictogram_ph_code ppc ON ppc.id_pictogram == p.id "
                                "join ph_code pc on pc.id == ppc.id_PH_Code "
                                "join classification_code cc ON cc.id_ph_code ==pc.id "
                                "join classification c on cc.id_classification ==c.id "
                                "join item i on c.id ==i.classification_id "
                                "where i.id == (:i_id)"),{"i_id": i.id})
            for r in res:
                pics.append(r[0])

        pics = list(set(pics))
        i.pictogram_paths = pics

    return items