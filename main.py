class Student:
    def __init__(self, first_lastname, teacher_class):
        self.first_lastname = first_lastname
        self.teacher_class = teacher_class


class Teacher:
    def __init__(self, teacher_first_lastname, teach, subject):
        self.teacher_first_lastname = teacher_first_lastname
        self.teach = teach
        self.subject = subject


class Homeroom:
    def __init__(self, homeroom_teach, homeroom_subject, homeroom_first_last):
        self.homeroom_teach = homeroom_teach
        self.homeroom_subject = homeroom_subject
        self.homeroom_first_last = homeroom_first_last


teachers_library = []
homeroom_teachers = []
students_library = []


while True:
    first_select = input("Select a command create/manage/end: ")
    if first_select == "end":
        print("Exiting the program...")
        break
    elif first_select == "create":
        second_select = input("Select student/teacher/homeroom teacher: ")
        if second_select == "student":
            first_lastname = input("Enter your first and lastname: ")
            teacher_class = input("Write what classes you are gonna have and what teachers to the classes: ")
            new_student = Student(first_lastname=first_lastname, teacher_class=teacher_class)
            students_library.append(new_student)

        if second_select == "teacher":
            teacher_first_lastname = input("Write in your first and last name: ")
            teach = input("What classes are you gonna attend: ")
            subject = input("What subject are you gonna teach: ")
            new_teacher = Teacher(teacher_first_lastname=teacher_first_lastname, teach=teach, subject=subject)
            teachers_library.append(new_teacher)

        if second_select == "homeroom teacher":
            homeroom_first_last = input("Write in your first and last name: ")
            homeroom_teach = input("What classes are you gonna attend: ")
            homeroom_subject = input("What subject are you gonna teach: ")
            new_homeroom_teacher = Homeroom(homeroom_teach=homeroom_teach, homeroom_subject=homeroom_subject,
                                            homeroom_first_last=homeroom_first_last)
            homeroom_teachers.append(new_homeroom_teacher)

    elif first_select == "manage":
        third_select = input("Select student/teacher/homeroom teacher/class/end: ")
        if third_select == "class":
            print(students_library, "homeroom_first_last")

        if third_select == "student":
            print(students_library, "teacher_first_lastname")

        if third_select == "teacher":
            print(teachers_library)

        if third_select == "homeroom teacher":
            print(homeroom_teachers)

        if third_select == "end":
            print("Exiting the program...")
            break
