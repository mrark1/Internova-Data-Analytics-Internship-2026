"""
Task 8: Basic File Handling
------------------------------
This program creates a text file, writes an introduction into it,
and then reads and displays the file contents.
"""

file_name = "introduction.txt"

# Writing to the file
introduction = (
    "Hi, my name is Aarav Sharma. I am a Computer Science student "
    "learning Python for Data Analytics. I am passionate about "
    "exploring data, building models, and solving real-world problems."
)

with open(file_name, "w") as file:
    file.write(introduction)

print(f"'{file_name}' created and introduction written successfully.\n")

# Reading and displaying the file contents
with open(file_name, "r") as file:
    content = file.read()

print("----- File Contents -----")
print(content)
