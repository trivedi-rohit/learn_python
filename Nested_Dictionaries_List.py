# Nested Dictionary
student_data = {
    "Ram": {"roll_no":10, "age":20, "course": "python"},
    "Mohan": {"roll_no":20, "age":22, "course": "Java"}    
}
print(student_data["Mohan"])
print(student_data["Ram"]["age"])
student_data["Mohan"]["phone_no"] = 9876543
print(student_data["Mohan"])
del student_data["Mohan"]["phone_no"]
print(student_data["Mohan"].pop("age"))
print(student_data["Mohan"])

# Nested List in a Dictionarry
Travel_data={
    "Gujrat":["Somnath", "Dwarkadhish", "Statue of Unity"],
    "Rajasthan" : ["Jaipur", "Jodhpur", "Udaipur", "Mount Abu"]
}
print(Travel_data["Rajasthan"])

# Nested Dictionary in List
std_data = [
    {"Name":"Karan","roll_no":15,"age":14,"course":"C#","Phone_no":[98769, 757658]},
    {"Name":"Vijay","roll_no":11,"age":22,"course": "Kotlin"}
]
print(std_data[0])
print(std_data[0]["Phone_no"])

# Nested Dictionaries & List exercise:
student_data= [
    {
        "Name":"Raju",
        "Age":14,
        "Roll_no":26,
        "Course":"Python"
    },
    {
        "Name":"Mohan",
        "Age":18,
        "Roll_no":35,
    }
]
def add_new_student(name, rollno, age, course):
    new_student={}
    new_student["Name"]=name
    new_student["Roll_no"]= rollno
    new_student["Age"]=age
    new_student["Course"]=course
    student_data.append(new_student)

add_new_student("Shyam",22,18,"C++")
print(student_data)


