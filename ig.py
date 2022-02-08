# CREATE A FUNCTION THAT TAKES IN A LIST OF STUDENTS AND PRINTS OUT THE STUDENT'S NAME AND GRADE

def student_grade(students):
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
        