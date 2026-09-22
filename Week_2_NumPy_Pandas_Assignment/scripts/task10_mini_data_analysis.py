import numpy as np
import pandas as pd
from pathlib import Path

df = pd.read_csv("../datasets/student_performance.csv")

print("1. DATASET LOADED")
print(df)

print("\n2. DATA INSPECTION")
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Missing values:\n", df.isna().sum())

# The dataset has no missing values, but this operation demonstrates safe handling.
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\n3. FILTERED STUDENTS (Marks >= 85)")
high_performers = df[df["Marks"] >= 85]
print(high_performers[["Name", "Department", "Marks", "Attendance"]])

print("\n4. SORTED BY MARKS (DESCENDING)")
print(df.sort_values("Marks", ascending=False)[["Name", "Marks"]])

print("\n5. GROUPBY DEPARTMENT")
group_summary = df.groupby("Department").agg(
    Average_Marks=("Marks", "mean"),
    Average_Attendance=("Attendance", "mean"),
    Student_Count=("Student_ID", "count")
).round(2)
print(group_summary)

print("\n6. PIVOT TABLE")
pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    columns="City",
    aggfunc="mean",
    fill_value=0
).round(2)
print(pivot)

print("\n7. KEY INSIGHTS")
print("Overall average marks:", round(df["Marks"].mean(), 2))
print("Highest marks:", df.loc[df["Marks"].idxmax(), "Name"], "-", df["Marks"].max())
print("Lowest marks:", df.loc[df["Marks"].idxmin(), "Name"], "-", df["Marks"].min())
best_dept = df.groupby("Department")["Marks"].mean().idxmax()
print("Department with highest average marks:", best_dept)
print("Students scoring 85 or above:", len(high_performers))

out = Path("../outputs/mini_project_cleaned.csv")
df.to_csv(out, index=False)
group_summary.to_csv("../outputs/mini_project_groupby.csv")
pivot.to_csv("../outputs/mini_project_pivot.csv")
print("\nCleaned dataset exported to:", out.resolve())
