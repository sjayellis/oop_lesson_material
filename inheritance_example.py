class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.id = self.generate_id()

    def generate_id(self):
        id_hash = 0
        for char in self.name:
            id_hash += ord(char)
        for char in self.surname:
            id_hash += ord(char)
        return id_hash % 1000000000

    def __str__(self):
        return f'{self.surname}, {self.name}\nID: {self.id}\nCourses:\n{self.courses}'

class Student(Person):
    #def __init__(self, name, surname):
    #    super().__init__(name, surname)

    def enroll(self, new_course):
        self.courses.append(new_course)

    #def __str__(self):
    #    return f'{self.surname}, {self.name}\nCourses:\n{self.courses}'

class Faculty(Person):
    def __init__(self, name, surname, position, salary):
        #self.name = name
        #self.surname = surname
        self.position = position
        self.salary = salary
        #self.courses = []
        super().__init__(name, surname)

    def assign_course(self, new_course):
        self.courses.append(new_course)

    def __str__(self):
        return super().__str__() + f'\nPosition: {self.position}\nSalary: {self.salary}'

student1 = Student("Sam", "Ellis")
faculty1 = Faculty("John", "Smith", "Professor", 60000)
print(student1)
print(faculty1)
#print(student1.id)