"""
Task 4: Conditional Statements
---------------------------------
This program takes marks as input and displays the grade using
if, elif, and else statements.

Grading Scheme:
90+     -> A
75-89   -> B
60-74   -> C
Below 60 -> Fail
"""

marks = float(input("Enter your marks (out of 100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"\nMarks obtained : {marks}")
print(f"Grade          : {grade}")
