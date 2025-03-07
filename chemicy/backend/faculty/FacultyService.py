import reflex as rx
import sqlalchemy

from chemicy.backend.department.DepartmentDto import DepartmentDto
from chemicy.backend.faculty.FacultyDto import FacultyDto


def get_all_faculties():
    d1_1 = DepartmentDto(id = 0, name= "Department 1")
    d1_2 = DepartmentDto(id = 1, name= "Department 2")
    d1_3 = DepartmentDto(id = 2, name= "Department 3")

    f1 = FacultyDto(id = 0, name = 'Rau1', departments= [d1_1, d1_2, d1_3])

    d2_1 = DepartmentDto(id=3, name="Department 4")
    d2_2 = DepartmentDto(id=4, name="Department 5")
    d2_3 = DepartmentDto(id=5, name="Department 6")

    f2 = FacultyDto(id=1, name='Rau2', departments=[d2_1, d2_2, d2_3])

    return [f1, f2]

def get_all_faculties_db():
    faculties = []
    with rx.session() as session:
        res = session.execute(
            sqlalchemy.text("SELECT * from faculty f  "))
        for r in res:
            dep_res = session.execute(
                sqlalchemy.text("SELECT * from department d "
                                "where d.faculty_id == (:idf)"),{"idf":r[0]}
            )
            deps = []
            for d in dep_res:
                deps.append(DepartmentDto(id=d[0], name=d[1]))

            faculties.append(FacultyDto(id = r[0], name=r[1], departments = deps))

    return faculties
