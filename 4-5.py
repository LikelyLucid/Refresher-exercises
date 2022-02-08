students = []
while True:
    Student = input("Enter the name of the student: ")
    if Student == "X":
        break
    print(Student)
    Grade = int(input("Enter the grade of the student: "))
    print(Grade)
    students.append([Student, Grade])

print("The average grade is:", sum(student[1] for student in students) / len(students)) #get average grade by summing all grades and dividing by number of students
print("The best grade is:", max(student[1] for student in students))

# Number 6
for student in students:
    student = student[0]
    grade = student[1]
    print(student, grade)
    # convert grade to interger
    grade = int(float(grade))
    # give grades a letter grade
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