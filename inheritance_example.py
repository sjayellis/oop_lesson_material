from abc import ABC, abstractmethod

class Person(ABC):
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

    @abstractmethod
    def expertise(self):
        raise NotImplementedError

    def __str__(self):
        return f'{self.surname}, {self.name}\nID: {self.id}\nCourses:\n{self.courses}'

class Student(Person):
    #def __init__(self, name, surname):
    #    super().__init__(name, surname)

    def enroll(self, new_course):
        self.courses.append(new_course)

    def expertise(self):
        knowledge = 'Courses Taken: '
        for course in self.courses:
            knowledge += f'{course}, '
        return knowledge

    #def __str__(self):
    #    return f'{self.surname}, {self.name}\nCourses:\n{self.courses}'

class Faculty(Person):
    def __init__(self, name, surname, position, salary, degrees):
        #self.name = name
        #self.surname = surname
        self.position = position
        self.salary = salary
        self.degrees = degrees
        #self.courses = []
        super().__init__(name, surname)

    def assign_course(self, new_course):
        self.courses.append(new_course)

    def expertise(self):
        knowledge = 'Degrees: '
        for degree in self.degrees:
            knowledge += f'{degree}, '
        knowledge += '\nCourses Taught: '
        for course in self.courses:
            knowledge += f'{course}'
        return knowledge

    def __str__(self):
        return super().__str__() + f'\nPosition: {self.position}\nSalary: {self.salary}'

student1 = Student("Sam", "Ellis")
faculty1 = Faculty("John", "Smith", "Professor", 60000, ['Bachelors in CS', 'PhD in CS'])
print(student1)
print(student1.expertise())
print(faculty1)
print(faculty1.expertise())
#print(student1.id)