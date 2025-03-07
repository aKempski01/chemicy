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
