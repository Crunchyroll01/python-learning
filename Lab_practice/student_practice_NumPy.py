import numpy as np
"""
def practice_5a_temperature_analysis():
    print("\n" + "="*50)
    print("EXERCISE 5.1: Finding Temperature Patterns")
    print("="*50)

    # Daily temperatures for two weeks
    temps = np.array([68, 72, 75, 71, 80, 82, 79,
    77, 73, 70, 69, 74, 78, 76])
    print("Two weeks of temperatures:", temps)

    # TODO 1: Find how many days were above 75°F
    # Use: np.sum(temps > 75)
    hot_days = np.sum(temps > 75)

    # TODO 2: Find the temperatures on cool days (below 70°F)
    # Use: temps[temps < 70]
    cool_temps = temps[temps < 70]

    # TODO 3: Find days with perfect weather (70-75°F)
    # Use: (temps >= 70) & (temps <= 75)
    perfect_days = (temps >= 70) & (temps <= 75)
    num_perfect = np.sum(perfect_days)

    # TODO 4: Find the position of the hottest day
    # Use: np.argmax(temps)
    hottest_day_index = np.argmax(temps)
    print(f"Days above 75°F: {hot_days}")
    print(f"Cool day temperatures: {cool_temps}")
    print(f"Number of perfect days: {num_perfect}")
    print(f"Hottest day was day #{hottest_day_index + 1 if hottest_day_index is not None else '?'}")
# Run this exercise
practice_5a_temperature_analysis()
"""


def practice_6_student_gradebook():
    print("\n" + "="*50)
    print("FINAL PROJECT: Class Gradebook System")
    print("="*50)

# Student grades: 6 students × 4 assignments
grades = np.array([
[88, 92, 85, 90], # Student 1
[75, 80, 78, 82], # Student 2
[93, 95, 91, 94], # Student 3
[67, 70, 72, 68], # Student 4
[82, 85, 88, 86], # Student 5
[90, 88, 92, 89] # Student 6
])

print("Class Gradebook:")
print("Student HW1 HW2 HW3 HW4")
for i in range(len(grades)):
    print(f" #{i+1} ", end="")
for grade in grades[i]:
    print(f" {grade}", end="")
print()

# TODO 1: Calculate each student's average (per row)
# Use: np.mean(grades, axis=1)
student_averages = np.mean(grades, axis=1)
# TODO 2: Calculate each assignment's average (per column)
# Use: np.mean(grades, axis=0)
assignment_averages = np.mean(grades, axis=0)

# TODO 3: Find the highest grade in the class
# Use: np.max(grades)
highest_grade = np.max(grades)

# TODO 4: Count how many students have an average >= 85
# First calculate student_averages, then use >= 85
if student_averages is not None:
    honor_roll = student_averages >= 85
    num_honor_roll = np.sum(honor_roll)

# TODO 5: Add 5 bonus points to all grades (but cap at 100)
# Use: np.minimum(grades + 5, 100)
curved_grades = np.minimum(grades + 5, 100)

# Print your results
print("\n--- ANALYSIS RESULTS ---")
if student_averages is not None:
    print(f"Student averages: {student_averages}")
if assignment_averages is not None:
    print(f"Assignment averages: {assignment_averages}")
if highest_grade is not None:
    print(f"Highest grade: {highest_grade}")
if 'num_honor_roll' in locals() and num_honor_roll is not None:
    print(f"Students on honor roll: {num_honor_roll}")

# Show letter grades
if student_averages is not None:
    print("\n--- LETTER GRADES ---")
for i, avg in enumerate(student_averages):
    if avg >= 90:
        letter = 'A'
    elif avg >= 80:
        letter = 'B'
    elif avg >= 70:
        letter = 'C'
    else:
        letter = 'D'
print(f"Student #{i+1}: {avg:.1f} ({letter})")
# Run the final project
practice_6_student_gradebook()
