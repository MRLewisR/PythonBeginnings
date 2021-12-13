class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year

    def welcome(self):
        print(f"Welcome {self.firstName} {self.lastName} to the class of {self.graduationYear}")

x = Student("John", "Smith", 2021)
x.welcome()
