from typing import List

import reflex as rx

from chemicy.backend.department.DepartmentDto import DepartmentDto
from chemicy.backend.faculty.FacultyDto import FacultyDto
from chemicy.backend.faculty.FacultyService import get_all_faculties, get_all_faculties_db
from chemicy.backend.user.UserDto import UserDto

from chemicy.backend.user.UserService import create_user, check_email_exits

class RegisterState(rx.State):
    user: UserDto = UserDto()

    faculties: List[FacultyDto]
    faculty_names: List[str] = []
    departments: List[str]
    register_valid: bool = False

    def init_state(self):
        self.register_valid = False
        self.user = UserDto()
        self.faculties = get_all_faculties_db()
        self.faculty_names = [f.name for f in self.faculties]
        self.departments = []


    def init_department_list(self):
        self.departments = [d.name for d in  [f.departments for f in self.faculties if f.name == self.user.faculty][0]]

    def register_btn_clicked(self):
        if check_email_exits(self.user.email):
            return rx.toast.error("Podaj inny adres email!")

        r = create_user(self.user)
        if r:
            return rx.redirect("/")
        else:
            return rx.toast.error("Skontaktuj się z administracją")

    def update_register_valid(self):
        if self.validate_password() and "@" in self.user.email and self.user.name != "" and self.user.surname != "" and self.user.department != "" and self.user.faculty != "":
            self.register_valid = True
        else:
            self.register_valid = False

    def set_name(self, name):
        self.user.name = name
        self.update_register_valid()

    def set_surname(self, surname):
        self.user.surname = surname
        self.update_register_valid()

    def set_password(self, password):
        self.user.password = password
        self.update_register_valid()

    def validate_password(self) -> bool:

        if self.user.password is not None and len(self.user.password)> 7 and any(char.isdigit() for char in self.user.password) and any(char.isupper() for char in self.user.password):
            return True
        return False

    def set_email(self, email):
        self.user.email = email
        self.update_register_valid()

    def set_phone(self, phone):
        self.user.phone = phone

    def set_office_room(self, office_room):
        self.user.office_room = office_room

    def set_website(self, website):
        self.user.website = website

    @rx.event
    def set_department(self, department: str):
        """Change the select value var."""
        self.user.department = department

    @rx.event
    def set_faculty(self, faculty: str):
        self.user.faculty = faculty
        self.init_department_list()