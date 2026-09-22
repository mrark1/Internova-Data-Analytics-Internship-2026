import pandas as pd

df = pd.read_csv("../datasets/student_performance.csv")

print("Selected Columns:\n", df[["Name", "Department", "Marks"]])
print("\nSelected Rows (first 3):\n", df.iloc[:3])

print("\nStudents with Marks >= 85:\n", df[df["Marks"] >= 85])

filtered = df[(df["Marks"] >= 80) & (df["Attendance"] >= 90)]
print("\nStudents with Marks >= 80 AND Attendance >= 90:\n", filtered)

print("\nSorted by Marks - Ascending:\n", df.sort_values("Marks"))
print("\nSorted by Marks - Descending:\n", df.sort_values("Marks", ascending=False))
