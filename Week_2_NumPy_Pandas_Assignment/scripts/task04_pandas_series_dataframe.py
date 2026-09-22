import pandas as pd

series = pd.Series([85, 91, 78, 88, 95], index=["A","B","C","D","E"])
print("Pandas Series:\n", series)

df = pd.DataFrame({
    "Name": ["Aarav", "Diya", "Rohan", "Ananya", "Kabir"],
    "Department": ["CSE", "CSE", "AIML", "AIML", "CSE"],
    "Marks": [88, 76, 91, 67, 84]
})

print("\nOriginal DataFrame:\n", df)
print("\nColumn Names:", list(df.columns))
print("Index:", df.index)

df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]
print("\nUpdated DataFrame:\n", df)
