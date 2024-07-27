student_marks = {
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}
result = {}
for student in student_marks:
    marks = student_marks[student] #! taking marks from dict. and stored here.
    if marks > 90:
        result[student] = "A+"
    elif marks <= 90 and marks >= 81:
        result[student] = "A"
    elif marks <= 80 and marks >= 71:
        result[student] = "B+"
    elif marks <= 70 and marks >= 61:
        result[student] = "B"
    elif marks <= 61 and marks >= 51:
        result[student] = "C"
    elif marks <= 50 and marks >= 41:
        result[student] = "D"
    elif marks <= 40:
        result[student] = "F"
print(result)