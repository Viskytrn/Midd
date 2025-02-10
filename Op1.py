class Person:
    def __init__(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation

#Behaviour
    def speak(self):
        print(self.name,"is speaking")


#Creating an object

person1=Person("Mark",46,"Teacher")
print(person1.name)
person1.speak()
