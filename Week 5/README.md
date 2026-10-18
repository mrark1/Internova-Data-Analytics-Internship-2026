# Week 5 – Power BI & Business Intelligence (Retail Sales Analysis)

## Contents
| Path | Description |
|---|---|
| `Week5_PowerBI_Assignment.pdf` | Full report: all 7 tasks, DAX formulas and outputs, visuals, insights, recommendations |
| `data/raw_sales.csv, raw_customers.csv, raw_products.csv` | Raw tables to import into Power BI (contain deliberate data-quality issues) |
| `data/clean_*.csv` | Cleaned reference output of Task 2 |
| `code/PowerQuery_M_Code.pq` | Power Query (M) code for the three queries |
| `code/DAX_Measures.dax` | Calendar table, calculated columns and all measures |
| `code/generate_dataset.py`, `code/analyze.py` | Python used to generate the dataset and to cross-check every number in the report |
| `screens/` | Data model, individual visuals and dashboard layout images |

## Dataset
Synthetic retail dataset (Jan 2024 – Dec 2025): `Sales` (fact, 1,730 raw rows), `Customers` (150), `Products` (19).
Issues injected on purpose: 40 duplicate orders, 30 missing Quantity, 25 missing ShipMode, 15 Discounts stored as text ("15%"),
inconsistent PaymentMode casing, OrderDate stored as text (dd-mm-yyyy), 2 useless columns, upper-case customer names, 6 missing Segment values.

## Rebuild the .pbix in Power BI Desktop (about 45 minutes)
1. Copy the `data` folder to `C:\PowerBI_Week5\data` (or edit the path in the M code).
2. **Home → Transform data → New Source → Blank Query → Advanced Editor**: paste each query from `PowerQuery_M_Code.pq` (name them Sales, Customers, Products). **Close & Apply**.
3. **Modeling → New table**: paste the `Calendar` table from `DAX_Measures.dax`; Table tools → *Mark as date table*; sort `Month` by `MonthNo`.
4. **Model view**: create 1:* relationships Customers[CustomerID]→Sales[CustomerID], Products[ProductID]→Sales[ProductID], Calendar[Date]→Sales[OrderDate] (single direction).
5. Add the calculated columns (Sales Amount, Cost Amount, Profit, Discount Band) and the measures from `DAX_Measures.dax`.
6. Build the dashboard as listed in Task 6 of the PDF, then **File → Save as** `RetailSales_Dashboard.pbix`.
7. Take real screenshots (Win + Shift + S) of Model view, each visual and the dashboard and replace the images in the report/submission where required.

Expected check values: Total Sales ₹12,321,711.45 · Total Profit ₹2,252,522.48 · Orders 1,660 · Margin 18.28%.
