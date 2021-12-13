class Person:
    def __init__(self, name, age, occupation, location):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.location = location

        '''
        
        global aOrAn
    
        if occupation[0] == "A":
            aOrAn = "an"
        
        else:
            aOrAn = "a"

        '''

    def information(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old, and I work as a {self.occupation} in {self.location}.")

person1 = Person("John", 27, "Accountant", "London")
person2 = Person("Nigel", 43, "Doctor", "New York")
person3 = Person("Jeffrey", 32, "Software Engineer", "Paris")

person1.information()
person2.information()
person3.information()

'''
print(person1.name)
print(person2.age)
print(person3.occupation)
'''