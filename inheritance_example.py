class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []

    def enroll(self, new_course):
        self.courses.append(new_course)

    def __str__(self):
        return f'{self.surname}, {self.name}\nCourses:\n{self.courses}'

class Faculty:
    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.courses = []

    def assign_course(self, new_course):
        self.courses.append(new_course)

student1 = Student("Sam", "Ellis")
print(student1)