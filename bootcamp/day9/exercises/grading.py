# You have access to a database of student_scores in the format of a dictionary. The keys in 
# student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should 
# have a new dictionary called student_grades that should contain student names for keys 
# and their grades for values. The final version of the student_grades dictionary will be checked.
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_scores = {"Peter": 67, "Erick": 89, "Laia": 99, "Karel": 78}

student_grades = {}
for idx in student_scores:
    if student_scores[idx] > 90:
        student_grades[idx] = "Outstanding"
    elif student_scores[idx] > 80:
        student_grades[idx] = "Exceeds Expectations"
    elif student_scores[idx] > 70:
        student_grades[idx] = "Acceptable"
    else:
        student_grades[idx] = "Fail"

print(student_grades)
