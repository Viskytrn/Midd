course = ["MIT","Cybersecurity","DataScience"]
print(course)

#Accessing an element
print(course[2])

#Looping through an array
for a in course:
    print("Course is",a)

#Adding a new element into an array
course.append("Laravel")
print(course)

#Deleting an element from array

course.remove("Cybersecurity")
print(course)