class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary

    def details(self):
        print(self.name,"is the",self.position)

Employee1=Employee("John","CEO",45000)
print(Employee1.name,Employee1.position,Employee1.salary)
Employee2=Employee("Eunice","HR",50000)
print(Employee2.name,Employee2.position,Employee2.salary)
Employee3=Employee("Judy","Chair",60000)
print(Employee3.name,Employee3.position,Employee3.salary)
Employee4=Employee("Jesse","Sec",70000)
print(Employee4.name,Employee4.position,Employee4.salary)
