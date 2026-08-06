def heading(func):
    def wrapper(*args):
        print("Report")
        func(*args)
    return wrapper


class Report:
    template = "Simple Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def set_template(cls, name):
        cls.template = name

    def __str__(self):
        return "Template: " + Report.template + "\nTitle: " + self.title + "\nContent: " + self.content

    @heading
    def show(self):
        print(self)


Report.set_template("Student Report")

r1 = Report("Result", "Shreya scored 90 marks.")

r1.show()
