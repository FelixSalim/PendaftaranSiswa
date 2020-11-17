from datetime import datetime

#own module
from models import student, user
import system
import view

system.students = system.load_student_data()
system.users = system.load_user_data()

while not system.error:
	view.main_menu()