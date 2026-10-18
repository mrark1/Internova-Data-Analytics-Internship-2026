# Retail Sales & Business Performance Analytics

## Project overview
This end-to-end analytics capstone demonstrates a retail sales workflow: data inspection, cleaning, exploratory data analysis (EDA), visualization, business insights, and a Power BI dashboard build plan.

> **Dataset transparency:** `data/raw_sales.csv` is a synthetic demonstration dataset generated for this project. It does not represent a real retailer or real customer transactions. If your assignment strictly requires a real-world dataset, replace it with a suitable public dataset and rerun the notebook before submission.

## Problem statement
Retail teams need a clear view of sales, profit, order volume, product/category performance, and regional demand. This project demonstrates how a cleaned transaction table can be used to answer these questions and communicate results through a dashboard.

## Dataset description
- Rows in raw file: 1,203 (includes intentional data-quality issues and duplicates)
- Rows after cleaning: 1,190
- Date range: 2024-01-01 to 2025-12-30
- Fields: Order_ID, Order_Date, Region, Category, Product, Quantity, Unit_Price, Discount, Sales, Profit, Customer_Segment, Payment_Method.
- Currency is not specified; all monetary values are treated as generic currency units.

## Tools used
Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook, Power BI Desktop, Git, GitHub.

## Data cleaning process
1. Parsed order dates and numeric fields.
2. Removed duplicate rows.
3. Removed rows with missing critical identifiers/category/product/date.
4. Removed invalid quantities (≤ 0), negative unit prices, and discounts outside 0–100%.
5. Filled missing categorical fields with the mode.
6. Filled missing unit prices with the median.
7. Recalculated Sales = Unit_Price × Quantity × (1 − Discount).
8. Imputed missing Profit using category-level median profit margin, with global fallback.
9. Saved cleaned output to `data/cleaned_sales.csv`.

## Exploratory data analysis
- Descriptive statistics and data types are inspected in the notebook.
- Missing values and duplicates are counted before cleaning.
- Correlation analysis examines Quantity, Unit_Price, Discount, Sales, and Profit.
- IQR screening flags potential numeric outliers; flagged rows should be investigated rather than automatically removed.
- The analysis is descriptive. Correlation does not imply causation.

## Visualizations
Seven generated PNGs are in `visualizations/`:
1. Monthly sales trend
2. Sales by category
3. Sales by region
4. Top 10 products by sales
5. Sales vs profit scatter plot
6. Numeric correlation heatmap
7. Sales by customer segment

## Power BI dashboard
See `powerbi/POWER_BI_BUILD_GUIDE.md` and `powerbi/measures.dax`. The guide specifies KPI cards, visuals, slicers, formatting, and QA checks.

**Not included:** a compiled `.pbix` file. Create and save it in Power BI Desktop as `powerbi/retail_sales_dashboard.pbix`.

## Key insights (illustrative synthetic data)
- Total sales: 480,580.26 currency units.
- Total profit: 178,868.70 currency units; aggregate profit margin: 37.22%.
- Highest-sales category: Furniture.
- Highest-sales region: North.
- Highest-sales product: Desk.
- Best category by aggregate profit margin: Office Supplies; lowest: Technology.
- Highest-sales month: 2024-01; lowest-sales month: 2024-12.

Because the dataset is synthetic, these are demonstrations of the analysis workflow, not evidence about a real business.

## Business recommendations
1. **Inventory planning:** Use the month/category/region breakdown to align stock levels with recurring high-demand periods; validate against real stockout and lead-time data before making purchasing decisions.
2. **Margin-aware promotions:** Compare discount levels with profit margin by product/category. Avoid increasing discounts solely to grow revenue unless incremental profit or customer lifetime value improves.
3. **Product portfolio review:** Investigate low-sales products alongside margin, returns, and inventory holding cost before discontinuing them.
4. **Regional action:** Compare regional sales with store count, marketing spend, and population to avoid confusing raw sales size with true performance.

## Reproducibility
From the project root:
```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python src/data_analysis.py
jupyter notebook notebooks/retail_sales_analysis.ipynb
```

## Git workflow
See `docs/git_workflow.md` for exact commands and a suggested 3-commit sequence.

## Conclusion
This project provides a reproducible starter capstone combining data cleaning, EDA, charts, business recommendations, and a documented Power BI implementation plan. Replace the synthetic data with a cited public dataset if real-world data is mandatory, then regenerate all metrics and visuals.
