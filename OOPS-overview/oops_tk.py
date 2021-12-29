# student = {"name": "ralf", "grades": (72, 93, 80, 80, 95)}
#
# def average(numbers):
#     return sum(numbers)/len(numbers)
#
# print(average(student["grades"]))

# Above code can be made more usable by using class
class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades)/len(self.grades)


student1 = Student("Bob", (80, 72, 80, 93, 95))
student2 = Student("Stuart", (10, 10, 9, 9, 9))

print(student1.average_grades())
print(student2.average_grades())