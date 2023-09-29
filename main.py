class Student:
    def __init__(self, first_lastname, classes):
        self.first_lastname = first_lastname
        self.classes = classes


class Teacher:
    def __init__(self, teacher_first_lastname, subject, classes_taught):
        self.teacher_first_lastname = teacher_first_lastname
        self.subject = subject
        self.classes_taught = classes_taught


class Homeroom:
    def __init__(self, homeroom_lead, homeroom_first_last):
        self.homeroom_lead = homeroom_lead
        self.homeroom_first_last = homeroom_first_last


teachers_library = []
homeroom_teachers = []
students_library = []
classes = []
classes_taught = []


while True:
    first_select = input("Select a command create/manage/end: ")
    if first_select == "end":
        print("Exiting the program...")
        break
    elif first_select == "create":
        second_select = input("Select student/teacher/homeroom teacher: ")
        if second_select == "student":
            first_lastname = input("Enter your first and lastname: ")
            classes = input("Write what classes you are gonna attend: ")
            new_student = Student(first_lastname=first_lastname, classes=classes)
            students_library.append(new_student)

        if second_select == "teacher":
            teacher_first_lastname = input("Write in your first and last name: ")
            subject = input("What subject are you gonna teach: ")
            classes_taught = input("How many classes have you taught (Leave blank to finish): ")
            if not classes_taught:
                break
            new_teacher = Teacher(teacher_first_lastname=teacher_first_lastname, subject=subject,
                                  classes_taught=classes_taught)
            teachers_library.append(new_teacher)

        if second_select == "homeroom teacher":
            homeroom_first_last = input("Write in your first and last name: ")
            homeroom_lead = input("What classes are you gonna lead: ")
            new_homeroom_teacher = Homeroom(homeroom_lead=homeroom_lead,homeroom_first_last=homeroom_first_last)
            homeroom_teachers.append(new_homeroom_teacher)

    elif first_select == "manage":
        third_select = input("Select what you want to manage: student/teacher/homeroom teacher/class/end: ")
        if third_select == "class":
            classes = input("Enter the class to display: ")
            print(f"class {students_library}")
            print(f"Homeroom teacher: {homeroom_teachers}")
        else:
            print(f"Class {classes} not found.")

        if third_select == "student":
            first_lastname = input("Enter the students first and lastname: ")
            print(students_library, "teacher_first_lastname")
            print(f"Classes: {classes}")

        if third_select == "teacher":
            teacher_first_lastname = input("Enter the teachers first and lastname: ")
            for teacher_first_lastname in teachers_library:
                if teacher_first_lastname == teacher_first_lastname:
            print(f"Teacher: {teacher_first_lastname}")
            print(f"Classes taught: {classes_taught}")
        else:
            print("Teacher not found in the system.")

        if third_select == "homeroom teacher":
            homeroom_first_last = input("Enter the homeroom teachers first and lastname: ")
            for student in students_library:
                if student == homeroom_teachers:

            print(f"Homeroom teachers:{homeroom_teachers}")
            print(f"Classes they lead: {classes}")
            print(f"Students that are in those classes: {students_library}")
        else:
                print(f"Homeroom teacher {homeroom_teachers} not found in the system.")

        if third_select == "end":
            print("Exiting the program...")
            break
