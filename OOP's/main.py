class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hii, I'm {self.name}")

p1 = Person("Enes")

p1.greet()


class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length
    def Area(self):
        return self.height * self.length

calculate = Rectangle(5, 12)

print(calculate.Area())



class Pets:
    def __init__(self, name, age, species, breed, color):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.color = color
    def makeSound(self):void

        if result == "dog":
            print("Hum Hum")
        elif result == "kitten":
            print("Meow")

