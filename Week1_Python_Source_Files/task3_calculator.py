"""
Task 3: Operators
-------------------
A simple calculator program that performs Addition, Subtraction,
Multiplication, Division, and Modulus using two numbers entered by the user.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
modulus = num1 % num2 if num2 != 0 else "Undefined (division by zero)"

print("\n----- Calculator Results -----")
print(f"Addition       : {num1} + {num2} = {addition}")
print(f"Subtraction    : {num1} - {num2} = {subtraction}")
print(f"Multiplication : {num1} * {num2} = {multiplication}")
print(f"Division       : {num1} / {num2} = {division}")
print(f"Modulus        : {num1} % {num2} = {modulus}")
