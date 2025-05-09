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

    def makeSound(self):
        if self.species == "dog":
            print("Hum Hum")
        elif self.species == "kitten":
            print("Meow")
        else:
            print("Unknown Pet!")

    def __str__(self):
        return f"{self.name}, is a {self.age} {self.color} {self.breed} {self.species}"

Pet1 = Pets("Bob", "2 Years old", "dog", "Shephard", "Black")
Pet2 = Pets("Lara", "6 months old", "kitten", "Lynx", "black and brown" )

Pet1.makeSound()
print(Pet2)
Pet2.makeSound()

