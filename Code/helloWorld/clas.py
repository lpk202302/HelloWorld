class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grade = {"语文": 100, "数学": 90}

    def set_grade(self, course, grade):
        if course in self.grade:
            self.grade[course] = grade

zhang = Student("张三", 1001)
print(zhang.name)
print(zhang.grade)