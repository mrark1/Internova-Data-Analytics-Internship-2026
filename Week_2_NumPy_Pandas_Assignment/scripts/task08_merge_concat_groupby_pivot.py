import pandas as pd

jan = pd.read_csv("../datasets/sales_january.csv")
feb = pd.read_csv("../datasets/sales_february.csv")

# Merge using a common column (Product) with a small product-category lookup.
product_info = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Category": ["Computer", "Accessory", "Accessory", "Display"]
})
merged = pd.merge(pd.concat([jan, feb], ignore_index=True), product_info, on="Product", how="left")

print("MERGED DATAFRAME\n", merged)

concatenated = pd.concat([jan, feb], ignore_index=True)
print("\nCONCATENATED DATAFRAME\n", concatenated)

grouped = concatenated.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Average_Sales=("Sales", "mean"),
    Order_Count=("Order_ID", "count"),
    Maximum_Sale=("Sales", "max")
).reset_index()
print("\nGROUPBY SUMMARY\n", grouped)

pivot = pd.pivot_table(
    concatenated,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)
print("\nPIVOT TABLE\n", pivot)

merged.to_csv("../outputs/task08_merged.csv", index=False)
grouped.to_csv("../outputs/task08_groupby_summary.csv", index=False)
pivot.to_csv("../outputs/task08_pivot_table.csv")
