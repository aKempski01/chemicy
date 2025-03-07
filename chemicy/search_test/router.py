# from typing import List
#
# from chemicy.models.reagent import ReagentModel
# from chemicy.models.room_place import PlaceModel, RoomModel
# from chemicy.models.user import UserModel
#
#
# def get_reagents() -> List[ReagentModel]:
#
#     r1 = RoomModel(id = 0, room_name='301')
#     p1 = PlaceModel(id = 0, place_name='shelf 1', room=r1)
#     p1_2 = PlaceModel(id = 1, place_name='shelf 2', room=r1)
#     p1_3 = PlaceModel(id = 2, place_name='shelf 3', room=r1)
#
#     r2 = RoomModel(id = 1, room_name='302')
#     p2 = PlaceModel(id = 3, place_name='Fridge 1', room=r2)
#     p2_2 = PlaceModel(id = 4, place_name='Fridge 2', room=r2)
#
#     r3 = RoomModel(id = 2, room_name='303')
#     p3 = PlaceModel(id = 5, place_name='Desk 1', room=r3)
#     p3_2 = PlaceModel(id = 6, place_name='Desk 2', room=r3)
#     p3_3 = PlaceModel(id = 7, place_name='Shelf', room=r3)
#
#
#
#     r1 = ReagentModel(id=0, name='reagent 1',description='asd', place=p1, status = "OK", rights='Open', owner_id=0,
#                       H_class=['H302', 'H314', 'H317'], P_class=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
#     r2 = ReagentModel(id=1, name='reagent 2',description='asd', place=p1_2, status = "OK", rights='Open', owner_id=1,
#                       H_class=['H302', 'H314', 'H317'], P_class=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
#     r3 = ReagentModel(id=2, name='reagent 3',description='asd', place=p1_3, status = "Low Level", rights='Open', owner_id=0,
#                       H_class=['H302', 'H314', 'H317'], P_class=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
#     r4 = ReagentModel(id=3, name='reagent 4',description='asd', place=p2, status = "Delivery", rights='Private', owner_id=2,
#                       H_class=['H302', 'H314', 'H317'], P_class=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
#     r5 = ReagentModel(id=4, name='reagent 5',description='asd', place=p2_2, status = "Missing", rights='Open', owner_id=3,
#                       H_class=['H302', 'H314', 'H317'], P_class=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
#     r6 = ReagentModel(id=5, name='reagent 6',description='asd', place=p3, status = "To Buy", rights='Private', owner_id=5,
#                       H_class=['H302', 'H314', 'H317'], P_class=['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338'])
#
#     return [r1, r2, r3, r4, r5, r6]
#
#
# def get_users() -> List[UserModel]:
#
#     u1 = UserModel(id=0, name = "Jan", surname= "Kowalski", reagents=[])
#     u2 = UserModel(id=1, name = "Maria", surname= "Nowak", reagents=[])
#     u3 = UserModel(id=2, name = "Gustaf", surname= "Kowalski", reagents=[])
#     u4 = UserModel(id=3, name = "Janusz", surname= "Nowak", reagents=[])
#     u5 = UserModel(id=4, name = "Anna", surname= "Kołodziej", reagents=[])
#     u6 = UserModel(id=5, name = "Marek", surname= "Kowalski", reagents=[])
#
#     return [u1, u2, u3, u4, u5, u6]
#
#
# def get_logged_user() -> UserModel:
#     u1 = UserModel(id=0, name = "Jan", surname= "Kowalski", reagents=[])
#     return u1
#
#
# def get_rooms() -> List[RoomModel]:
#     r1 = RoomModel(id = 0, room_name='301')
#     r2 = RoomModel(id = 1, room_name='302')
#     r3 = RoomModel(id = 2, room_name='303')
#
#     return [r1, r2, r3]
#
# def get_places_for_room_id(room_id: int) -> List[PlaceModel]:
#     r1 = RoomModel(id = 0, room_name='301')
#     p1 = PlaceModel(id = 0, place_name='shelf 1', room=r1)
#     p1_2 = PlaceModel(id = 1, place_name='shelf 2', room=r1)
#     p1_3 = PlaceModel(id = 2, place_name='shelf 3', room=r1)
#
#     r2 = RoomModel(id = 1, room_name='302')
#     p2 = PlaceModel(id = 3, place_name='Fridge 1', room=r2)
#     p2_2 = PlaceModel(id = 4, place_name='Fridge 2', room=r2)
#
#     r3 = RoomModel(id = 2, room_name='303')
#     p3 = PlaceModel(id = 5, place_name='Desk 1', room=r3)
#     p3_2 = PlaceModel(id = 6, place_name='Desk 2', room=r3)
#     p3_3 = PlaceModel(id = 7, place_name='Shelf', room=r3)
#     places = [p1, p1_2, p1_3, p2, p2_2, p3, p3_2, p3_3]
#     places = [p for p in places if p.room.id == room_id]
#     return places
