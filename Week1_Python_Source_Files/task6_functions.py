"""
Task 6: Functions
-------------------
Two user-defined functions:
1. square(number) -> calculates the square of a number.
2. average(a, b, c) -> calculates the average of three numbers.
Both functions are called using user input.
"""

def square(number):
    """Returns the square of the given number."""
    return number ** 2


def average(a, b, c):
    """Returns the average of three numbers."""
    return (a + b + c) / 3


# Calling square()
num = float(input("Enter a number to find its square: "))
print(f"Square of {num} = {square(num)}")

# Calling average()
n1 = float(input("\nEnter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
print(f"Average of {n1}, {n2}, {n3} = {average(n1, n2, n3)}")
