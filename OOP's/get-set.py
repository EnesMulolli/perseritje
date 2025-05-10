class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

student1 = Student("Enes", 17)
print("Name:", student1.get_name())
print("Age:", student1.get_age(), "Years Old")


student1.set_name("Harry")
print("Changed name to:", student1.get_name())

student1.set_age(22)
print("Changed age to:", student1.get_age())