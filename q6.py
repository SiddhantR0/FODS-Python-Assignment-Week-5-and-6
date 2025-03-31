'''
In this progeam, there is a function that defines a class Student and takes
input for Students from user in the obj and then shows the result/output. 
'''

# function for defining Student class
class Student:
    def __init__(self, student_id, name, address, admission_year, level, section):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def info_show(self):
        print("\nStudent Information:")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

# taking input from the user
student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
address = input("Enter Address: ")
admission_year = input("Enter Admission Year: ")
level = input("Enter Level: ")
section = input("Enter Section: ")

# object for class "Student"
student = Student(student_id, name, address, admission_year, level, section)

# displaying the result
student.info_show()
