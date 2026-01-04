# Marks and Grade Calculator
# Date: December 2024

print("=== Student Grade Calculator ===")
print()

# Constants
MAX_MARKS_PER_SUBJECT = 100

# Get marks for each subject
english_marks = int(input("Enter marks obtained in English (out of 100): "))
science_marks = int(input("Enter marks obtained in Science (out of 100): "))
maths_marks = int(input("Enter marks obtained in Maths (out of 100): "))

# Calculate totals
total_marks_obtained = english_marks + science_marks + maths_marks
total_possible_marks = MAX_MARKS_PER_SUBJECT * 3

# Calculate percentage
percentage = (total_marks_obtained * 100) / total_possible_marks

# Determine grade based on percentage
if percentage >= 90:
    grade = 'A'
    remark = 'Excellent!'
elif percentage >= 80:
    grade = 'B'
    remark = 'Very Good!'
elif percentage >= 70:
    grade = 'C'
    remark = 'Good'
elif percentage >= 60:
    grade = 'D'
    remark = 'Satisfactory'
else:
    grade = 'F'
    remark = 'Needs Improvement'

# Display results
print()
print("-" * 45)
print("REPORT CARD")
print("-" * 45)
print(f"English:    {english_marks}/{MAX_MARKS_PER_SUBJECT}")
print(f"Science:    {science_marks}/{MAX_MARKS_PER_SUBJECT}")
print(f"Maths:      {maths_marks}/{MAX_MARKS_PER_SUBJECT}")
print("-" * 45)
print(f"Total:      {total_marks_obtained}/{total_possible_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade:      {grade}")
print(f"Remark:     {remark}")
print("-" * 45)
