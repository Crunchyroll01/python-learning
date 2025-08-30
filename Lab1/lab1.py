""" # The Easy Difficulty
student_profile={}
print(f"Empty student profile: {student_profile}")
print(f"Type:{type(student_profile)}")
student_profile["name"]= "Cody Fancil"
print(f"After adding my name: {student_profile}")
student_profile["age"]= 23
print(f"After adding my age: {student_profile}")
student_profile["Favorite Subject"]="Psychology"
print(f"After adding my favorite subject: {student_profile}")
print("\n\n--- Accessing Information ---\n\n")
print(f"My name is: {student_profile["name"]}")
print(f"My age is: {student_profile["age"]}")
print(f"My fav subject is: {student_profile['Favorite Subject']}")
print("\n\n--- Your Turn ---\n\n")
student_profile["hometown"]=input("Enter your hometown: ")
student_profile["Hobby"]=input("Enter your hobby: ")
student_profile["year_in_School"]=input("Enter your school year (Sophmore.. etc.): ")
print(f"\n\nProfile completed: {student_profile}")
"""

"""
print("=== Multiple Ways to Create Dictionaries ===\n\n")
# Method 1: Literal syntax
student1={
    "name" : "Cody Fancil",
    "id" : 3234,
    "gpa" : 3.8,
    "major" : "Information Systems"
}
# Method 2: dict() constructor with keyword arguments
student2= dict(
    name = "Stacy",
    id = 2334,
    gpa = 4.0,
    major = "Computer Science"
)
"""
# Challenge Difficulty
# Create a course dictionary using at least 2 different methods
# Include: course_code, title, credits, instructor
cody_fancil={}
jerry={}
cody_fancil={
    "course_code": "CS1300",
    "title": "Computer Science 2",
    "credit_hour": 12,
    "instructor": "Xin Wang"
}
jerry={
    "course_code": "CS1300",
    "title": "Computer Science 2",
    "credit_hour": 15,
    "instructor": "Xin Wang"
}
Comp_Sci2={cody_fancil,jerry}