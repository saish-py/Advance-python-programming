class Course:
    def __init__(self, course_name, duration, fee):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee
        self.category = self.categorize_course()

    def categorize_course(self):
        if self.duration <= 6:
            return "Short-Term"
        else:
            return "Long-Term"

    def display(self):
        print("Course Name :", self.course_name)
        print("Duration    :", self.duration, "months")
        print("Fee         :", self.fee)
        print("Category    :", self.category)

class Institute:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print("\nCourse Details")
        for course in self.courses:
            course.display()

institute = Institute()
n = int(input("Enter number of courses: "))

for i in range(n):
    print(f"\nEnter details of Course {i + 1}")
    course_name = input("Course Name: ")
    duration = int(input("Duration (in months): "))
    fee = float(input("Fee: "))

    course = Course(course_name, duration, fee)
    institute.add_course(course)

institute.display_courses()
