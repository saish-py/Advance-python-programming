class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display(self):
        print("Roll Number :", self.roll_no)
        print("Name        :", self.name)
        print("Marks       :", self.marks)
        print("Grade       :", self.grade)

class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("\nStudent Details")
        for student in self.students:
            student.display()

college = College()

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i + 1}")
    roll_no = int(input("Roll Number: "))
    name = input("Name: ")
    marks = float(input("Marks: "))

    student = Student(roll_no, name, marks)
    college.add_student(student)

college.display_students()
