"""

Dog:
    Attributes:
        - Breed
        - Weight
        - Energy

Bilbo Waggins:
    Attributes:
        - Labrador
        - 80 lbs
        - Low

"""

class Dog:
    energy = "High"

    def speak(self):
        print("Woof")

bilboWaggins = Dog() #Object is created

print(bilboWaggins.energy)
bilboWaggins.speak()

chewbarka = Dog()
chewbarka.energy = "Low"
print(chewbarka.energy)
chewbarka.speak()

####################################################################################################################

class Dog:
    def __init__(self, name, breed, energy): #Need to pass in name, breed, and energy parameters when creating an object
        self.name = name
        self.breed = breed
        self.energy = energy

dog1 = Dog("Ross Barkley", "Jack Russell", "High")

print(dog1.name)
print(dog1.breed)

####################################################################################################################

_money = 10000000

class Feline:
    __family = "Felidae" #Underscores avoid clashes

kitty = Feline()
print(kitty._Feline__family) #Need underscores

####################################################################################################################

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

Lewis = Student("Lewis", "18")

print(getattr(Lewis, "age"))

####################################################################################################################

class Athlete:
    def __init__(self, name):
        self.name = name

class Footballer(Athlete):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

player1 = Footballer("John", "Man U")

print(player1.team)

####################################################################################################################

#Overriding

class Animal:
    offspring = 0

    def reproduce(self):
        self.offspring += 1

class Dog(Animal):
    def reproduce(self):
        self.offspring += 6

john = Dog()
john.reproduce()
print(john.offspring)

####################################################################################################################

from abc import ABC, abstractmethod #Allows us to create abstract classes

class Bird(ABC):
    fly = True
    offspring = 0

    def noise(self):
        return 'Squawk'
    
    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):
    def reproduce(self):
        self.offspring += 6

    def eat(self):
        return "Peck Peck"

class Dodo(Bird):
    fly = False
    extinct = True

    def eat(self):
        return "Nom Nom"

    def reproduce(self):
        if not self.extinct:
            self.offspring += 1

Birdie = Dodo()

print(Birdie.fly)