"""
Task 7: Strings & Collections
--------------------------------
Demonstrates:
- String operations: upper(), lower(), replace(), find()
- List operations: append(), remove(), sort()
- Tuple creation and indexing
- Dictionary storing student information
- Set operations: add(), remove()
"""

# ---------- String Operations ----------
print("===== String Operations =====")
text = "Python for Data Analytics"
print("Original String :", text)
print("Uppercase       :", text.upper())
print("Lowercase       :", text.lower())
print("Replace         :", text.replace("Data Analytics", "Data Science"))
print("Find 'Data'     : index", text.find("Data"))

# ---------- List Operations ----------
print("\n===== List Operations =====")
fruits = ["Mango", "Apple", "Banana"]
print("Original List   :", fruits)

fruits.append("Orange")
print("After append()  :", fruits)

fruits.remove("Banana")
print("After remove()  :", fruits)

fruits.sort()
print("After sort()    :", fruits)

# ---------- Tuple Creation and Indexing ----------
print("\n===== Tuple Operations =====")
coordinates = (10, 20, 30, 40)
print("Tuple           :", coordinates)
print("First element   :", coordinates[0])
print("Last element    :", coordinates[-1])
print("Slice [1:3]     :", coordinates[1:3])

# ---------- Dictionary storing student information ----------
print("\n===== Dictionary Operations =====")
student = {
    "name": "Aarav Sharma",
    "age": 21,
    "branch": "Computer Science",
    "cgpa": 8.7
}
print("Student Dictionary:", student)
for key, value in student.items():
    print(f"{key} : {value}")

# ---------- Set Operations ----------
print("\n===== Set Operations =====")
skills = {"Python", "SQL", "Excel"}
print("Original Set    :", skills)

skills.add("Power BI")
print("After add()     :", skills)

skills.remove("Excel")
print("After remove()  :", skills)
