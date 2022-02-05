"""Your English teacher wants a program to keep track of their student marks and grades. Write a program which takes, as input, the student's name and an exam mark — between 0 and 100. The program should keep asking for input until "X" is entered as the student name. The program should then output the name and mark of the best student, as well as the average mark for all students.
"""

students = []
while True:
    Student = input("Enter the name of the student: ")
    if Student == "X":
        break
    print(Student)
    Grade = int(input("Enter the grade of the student: "))
    print(Grade)
    students.append([Student, Grade])
print("The average grade is:", sum(student[1] for student in students) / len(students))
print("The best grade is:", max(student[1] for student in students))

for student in students:
    student = student[0]
    grade = student[1]
    print(student, grade)
    # convert grade to interger
    grade = int(float(grade))
    if grade >= 90:
        final_grade = "A+"
    elif grade >= 85:
        final_grade = "A"
    elif grade >= 80:
        final_grade = "A-"
    elif grade >= 75:
        final_grade = "B+"
    elif grade >= 70:
        final_grade = "B"
    elif grade >= 65:
        final_grade = "B-"
    elif grade >= 60:
        final_grade = "C+"
    elif grade >= 55:
        final_grade = "C"
    elif grade >= 50:
        final_grade = "C-"
    elif grade >= 40:
        final_grade = "D"
    else:
        final_grade = "E"

    print(student," - " ,final_grade)