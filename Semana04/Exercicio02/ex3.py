

class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def addStudent(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def getList(self):
        return self.students.copy()

    def getAvrGrade(self):
        sum = 0
        for student in self.students:
            sum += student.get_grade()
        return sum/len(self.students)


s1 = student("Bill",22,99)
s2 = student("Ana",25,60)
s3 = student("Bia",18,100)


crs = Course("Science",2)
crs.addStudent(s1)
crs.addStudent(s2)
print(crs.students)
print(crs.students[0].name)
print(crs.getAvrGrade())


