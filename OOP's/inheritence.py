class Animal:
    def sound(self):
        print("Animal Sounds")

class Dog(Animal):
    def sound(self):
        print("Hum Hum")

class Cat(Animal):
    def sound(self):
        print("Meow")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()