#Built in functions/Standard library functions

y= max(67,43,89,90,23)
print("The max value is",y)

x=min(15,3,20,78)
print("The minimum value is",x)

#User defined functions
def name():
    print("Vince Gitonga")

name() #Calling a function


def multiply():
    x=10
    y=2
    print(x*y)
multiply()


#Parameter/Variable and Arguments/Value

def add(a,b):
     print(a+b)

add(1,4)
add(6,7)

def employee(Name, Gender, Position, Salary):
    print(Name,Gender,Position,Salary)
employee("Mark","Male","Chairman","60000")
employee("Mary","Female","Chairman","50000")
employee("May","Male","Chairlady","40000")

#Write a program that displays details of five students
#Use a user defined function with the help of parameter and arguments

def Student(Fullname,Age,Course,Gender):
    print(Fullname,Age,Course,Gender)
Student("Rodney Karani","18","MIT","Male")
Student("James Kyema","18","MIT","Male")
Student("Wayne Murimi","18","MIT","Male")
Student("Caleb Munene","18","MIT","Male")
Student("Ruciano Mkubwa","18","MIT","Male")


