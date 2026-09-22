import pandas as pd

df = pd.read_csv("../datasets/student_performance.csv")

print("First 5 Rows:\n", df.head())
print("\nLast 5 Rows:\n", df.tail())
print("\nNumber of Rows and Columns:", df.shape)
print("\nColumn Names:", list(df.columns))
print("\nData Types:\n", df.dtypes)
print("\nINFO")
df.info()
print("\nDESCRIPTIVE STATISTICS\n", df.describe())
