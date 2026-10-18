"""Retail Sales Analytics: reproducible cleaning and summary pipeline.
Run from project root: python src/data_analysis.py
Dataset is synthetic demonstration data; see README.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "visualizations"
OUT.mkdir(exist_ok=True)

def clean_data(path=DATA / "raw_sales.csv"):
    df = pd.read_csv(path)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    for col in ["Quantity", "Unit_Price", "Discount", "Sales", "Profit"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.drop_duplicates()
    df = df.dropna(subset=["Order_ID", "Order_Date", "Category", "Product"])
    df = df[(df["Quantity"] > 0) & (df["Unit_Price"] >= 0) & df["Discount"].between(0, 1)]
    for col in ["Region", "Customer_Segment", "Payment_Method"]:
        df[col] = df[col].fillna(df[col].mode().iloc[0])
    df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
    df["Discount"] = df["Discount"].fillna(df["Discount"].median())
    df["Sales"] = df["Unit_Price"] * df["Quantity"] * (1 - df["Discount"])
    ratios = df["Profit"] / df["Sales"].replace(0, np.nan)
    cat_margins = ratios.groupby(df["Category"]).median()
    global_margin = ratios.median()
    missing_profit = df["Profit"].isna()
    df.loc[missing_profit, "Profit"] = df.loc[missing_profit].apply(
        lambda row: row["Sales"] * cat_margins.get(row["Category"], global_margin), axis=1
    )
    df["Sales"] = df["Sales"].round(2)
    df["Profit"] = df["Profit"].round(2)
    return df

def main():
    df = clean_data()
    df.to_csv(DATA / "cleaned_sales_from_script.csv", index=False)
    df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
    print(f"Rows after cleaning: {len(df):,}")
    print(f"Total sales: {df['Sales'].sum():,.2f}")
    print(f"Total profit: {df['Profit'].sum():,.2f}")
    print(f"Unique orders: {df['Order_ID'].nunique():,}")
    print(f"Units sold: {df['Quantity'].sum():,}")
    print(f"Overall profit margin: {df['Profit'].sum()/df['Sales'].sum():.2%}")
    print("\nCategory summary:\n", df.groupby("Category").agg(
        Sales=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Order_ID", "nunique")
    ).sort_values("Sales", ascending=False))
    chart = df.groupby("Month")["Sales"].sum()
    ax = chart.plot(figsize=(11, 4), marker="o", title="Monthly Sales Trend")
    ax.set_xlabel("Month"); ax.set_ylabel("Sales (currency units)")
    plt.tight_layout(); plt.savefig(OUT / "monthly_sales_from_script.png", dpi=160); plt.close()

if __name__ == "__main__":
    main()
