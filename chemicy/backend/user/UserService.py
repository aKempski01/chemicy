from typing import List, Optional
import reflex as rx
import sqlalchemy

from chemicy.backend.user.UserDto import UserDto


def get_all_users() -> List[UserDto]:
    u1 = UserDto(id=0, name = "Jan", surname= "Kowalski", items=[])
    u2 = UserDto(id=1, name = "Maria", surname= "Nowak", items=[])
    u3 = UserDto(id=2, name = "Gustaf", surname= "Kowalski", items=[])
    u4 = UserDto(id=3, name = "Janusz", surname= "Nowak", items=[])
    u5 = UserDto(id=4, name = "Anna", surname= "Kołodziej", items=[])
    u6 = UserDto(id=5, name = "Marek", surname= "Kowalski", items=[])

    return [u1, u2, u3, u4, u5, u6]

def get_logged_user() -> UserDto:
    u1 = UserDto(id=0, name = "Jan", surname= "Kowalski", items=[])
    return u1



def get_all_user_db() -> List[UserDto]:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT u.id, u.email, u.name, u.surname, u.office_room, u.telephone_number, u.website, us.name "
                "FROM user u "
                "JOIN user_status us ON us.id == u.status_id "
            )
        )

    users = []
    for r in res:
        user = UserDto(id = r[0], email=r[1], name=r[2], surname=r[3], office_room=r[4], phone=r[5], website=r[6], status=r[7])
        users.append(user)

    return users



def validate_user(user_email, user_password) -> bool:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT u.email, u.password "
                "FROM user u "
                "WHERE u.email = (:email);"
            ),
            {"email": user_email},
        )

    for r in res:
        if r[1] == user_password:
            return True

    return False

def get_user_by_email(user_email: str) -> Optional[UserDto]:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT u.id, u.email, u.name, u.surname, u.office_room, u.telephone_number, us.name, ur.name "
                "FROM user u "
                "Join user_status us ON us.id ==u.status_id "
                "Join user_right ur ON ur.id = u.right_id "
                "WHERE u.email = (:email);"
            ),
            {"email": user_email},
        )

    for r in res:
        user = UserDto(id = r[0], email=r[1], name=r[2], surname=r[3], office_room=r[4], phone=r[5], status=r[6], rights=r[7])
        return user

    return None

def check_email_exits(user_email: str) -> bool:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT u.email "
                "FROM user u "
                "WHERE u.email = (:email);"
            ),
            {"email": user_email},
        )

    for r in res:
        return True
    return False


def get_user_statuses() -> List[dict]:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT us.id, us.name, us.color "
                "FROM user_status us;"
            ),
        )
    s = []
    for r in res:
        s.append({"id": r[0], "name": r[1], "color": r[2]})
    return s

def get_user_status_by_name(name: str) -> Optional[dict]:
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "SELECT us.id, us.name, us.color "
                "FROM user_status us "
                "WHERE us.name = (:name);"
            ),{"name": name},
        )
    for r in res:
        s = {"id": r[0], "name": r[1], "color": r[2]}
        return s
    return None

def create_user(user_dto: UserDto) -> bool:
    s = get_user_status_by_name("Pending")
    if s is None:
        print("Wrong status Name!!!")
        return False

    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text(
                "INSERT INTO user(name, surname, email, password, office_room, telephone_number, website, status_id) "
                "VALUES((:name), (:surname), (:email), (:password), (:office_room), (:telephone_number), (:website), (:status_id));"
            ),
            {"name": user_dto.name,"surname": user_dto.surname, "email": user_dto.email,"password": user_dto.password,"office_room":user_dto.office_room,
               "telephone_number": user_dto.phone, "website": user_dto.website, "status_id": s['id']},
        )
        session.commit()
    return True
