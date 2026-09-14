"""
Task 1: Python Basics
----------------------
This program prints a welcome message, takes the user's Name, College Name,
and Branch as input, and displays the entered information in a formatted output.
"""

print("=" * 50)
print("WELCOME TO PYTHON FUNDAMENTALS FOR DATA ANALYTICS")
print("=" * 50)

# Taking user input
name = input("Enter your Name: ")
college = input("Enter your College Name: ")
branch = input("Enter your Branch: ")

# Displaying formatted output
print("\n----- Student Details -----")
print(f"Name         : {name}")
print(f"College Name : {college}")
print(f"Branch       : {branch}")
print("-" * 28)
print(f"Hello {name}! Wishing you a great learning journey in Data Analytics.")
