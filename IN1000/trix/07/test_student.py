from student import Student
from random import randint

students_names = ["Joakim", "Dag", "Kristin", "Jonas", "Henrik", "Mats"]
students = []

for name in students_names:
    students.append(Student(name, 0, 0))
    
for i in range(5):
    for student in students:
        student.add_points(randint(1, 10))
for student in students:
    student.info()

