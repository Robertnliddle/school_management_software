


#Library

teachers_library = []
homeroom_teachers = []
students_library = []

while True:
    first_select = input("Select create/manage/end: ")
    if first_select == "end":
        break
    elif first_select == create:
        second_select = input("Select student/teacher/homeroom teacher: ")
