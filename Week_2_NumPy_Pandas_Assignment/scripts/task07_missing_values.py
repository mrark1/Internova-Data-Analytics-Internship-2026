import pandas as pd

df = pd.read_csv("../datasets/missing_values.csv")
print("DATASET BEFORE HANDLING MISSING VALUES\n", df)

print("\nMissing values by column:\n", df.isnull().sum())

removed = df.dropna()
print("\nAfter removing rows containing missing values:\n", removed)

filled = df.copy()
filled["Marks"] = filled["Marks"].fillna(filled["Marks"].mean())
filled["Attendance"] = filled["Attendance"].fillna(filled["Attendance"].mean())
filled["Department"] = filled["Department"].fillna(filled["Department"].mode()[0])

print("\nAfter filling missing values:\n", filled)

filled.to_csv("../outputs/task07_cleaned_missing_values.csv", index=False)

print("\nWhy is handling missing data important?")
print("Missing values can distort statistics, reduce model quality, and cause errors.")
print("Appropriate removal or imputation improves data completeness and analytical reliability.")
