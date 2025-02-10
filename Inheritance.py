#Parent/Super/Base class
class Animal:
    def speak(self):
        print("Animal is speaking")

#Child/Sub/Derived class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat:
    def meow(self):
        print("Cat is meowing")


a = Animal()
d = Dog()
d.speak()
c = Cat()
c.meow()