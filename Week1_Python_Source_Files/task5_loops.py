"""
Task 5: Loops
---------------
This program demonstrates:
1. Printing numbers from 1 to 20 using a for loop.
2. Printing the multiplication table of a number entered by the user.
3. Printing even numbers from 1 to 50 using a while loop.
"""

# 1. Print numbers from 1 to 20 using a for loop
print("----- Numbers from 1 to 20 -----")
for i in range(1, 21):
    print(i, end=" ")
print("\n")

# 2. Multiplication table of a number
num = int(input("Enter a number to print its multiplication table: "))
print(f"\n----- Multiplication Table of {num} -----")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. Even numbers from 1 to 50 using a while loop
print("\n----- Even numbers from 1 to 50 (while loop) -----")
n = 1
while n <= 50:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1
print()
