"""Your English teacher wants a program to keep track of their student marks and grades. Write a program which takes, as input, the student's name and an exam mark — between 0 and 100. The program should keep asking for input until "X" is entered as the student name. The program should then output the name and mark of the best student, as well as the average mark for all students.
"""

students = []
while True:
    Student = input("Enter the name of the student: ")
    if Student == "X":
        break
    Grade = int(input("Enter the grade of the student: "))
    students.append([Student, Grade])
print("The average grade is:", sum(student[1] for student in students) / len(students))
print("The best grade is:", max(student[1] for student in students))

for student in students:
    student = student[0]
    grade = student[1]
    # convert grade to interger
    grade = int(grade)