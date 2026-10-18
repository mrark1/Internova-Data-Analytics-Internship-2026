"""Generates the synthetic Retail Sales dataset (3 raw tables) used in the Week 5 Power BI assignment.
Raw files intentionally contain data-quality problems so the Power Query cleaning task is meaningful."""
import numpy as np, pandas as pd
rng = np.random.default_rng(42)

# ---------- Products ----------
cats = {
 "Electronics": [("Wireless Mouse",650,0.30),("Bluetooth Speaker",1800,0.28),("USB-C Charger",900,0.35),("Smart Watch",4500,0.22),("Headphones",2200,0.27),("Power Bank",1500,0.30)],
 "Furniture":   [("Office Chair",5200,0.18),("Study Table",6800,0.16),("Bookshelf",4200,0.20),("Floor Lamp",1900,0.32)],
 "Stationery":  [("Notebook Pack",240,0.45),("Gel Pen Box",180,0.50),("Desk Organizer",520,0.40),("Planner Diary",350,0.42),("Marker Set",300,0.44)],
 "Clothing":    [("Cotton T-Shirt",599,0.38),("Denim Jeans",1799,0.30),("Hoodie",1499,0.33),("Sports Shoes",2599,0.25)],
}
prod = []
pid = 101
for c, items in cats.items():
    for n, price, margin in items:
        prod.append(dict(ProductID=f"P{pid}", ProductName=n, Category=c, UnitPrice=price, UnitCost=round(price*(1-margin),2))); pid += 1
products = pd.DataFrame(prod)

# ---------- Customers ----------
cities = {"North":["Kanpur","Lucknow","Delhi","Jaipur"],"South":["Bengaluru","Chennai","Hyderabad"],
          "East":["Kolkata","Patna","Bhubaneswar"],"West":["Mumbai","Pune","Ahmedabad"]}
first = ["Aarav","Vivaan","Aditya","Ishaan","Rohan","Kabir","Ananya","Diya","Saanvi","Priya","Neha","Riya","Karan","Arjun","Meera","Sneha","Rahul","Pooja","Vikram","Anjali"]
last  = ["Sharma","Verma","Singh","Gupta","Patel","Reddy","Das","Iyer","Mishra","Khan","Joshi","Nair"]
cust=[]
for i in range(1,151):
    reg = rng.choice(list(cities), p=[.34,.22,.2,.24])
    cust.append(dict(CustomerID=f"C{1000+i}", CustomerName=f"{rng.choice(first)} {rng.choice(last)}",
                     Segment=rng.choice(["Consumer","Corporate","Home Office"],p=[.55,.30,.15]),
                     Region=reg, City=rng.choice(cities[reg])))
customers = pd.DataFrame(cust)

# ---------- Sales (fact) ----------
n = 2400
dates = pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0,731,n), unit="D")
month_w = {1:.9,2:.85,3:.95,4:.95,5:1,6:.95,7:.9,8:1,9:1.05,10:1.35,11:1.5,12:1.25}   # festive peak Oct-Dec
keep = rng.random(n) < np.array([month_w[d.month]/1.5 for d in dates])
dates = dates[keep]; n = len(dates)
pw = np.array([3,3,3,2,2,3,1,1,1,2,4,4,3,3,2,2,2,2,1,1][:len(products)],float) if False else None
pidx = rng.choice(len(products), n)
qty = rng.integers(1,8,n)
disc = rng.choice([0,0,0,0.05,0.10,0.15,0.20],n)
sales = pd.DataFrame(dict(
    OrderID=[f"ORD{50000+i}" for i in range(n)],
    OrderDate=dates, CustomerID=rng.choice(customers.CustomerID,n),
    ProductID=products.ProductID.values[pidx], Quantity=qty, Discount=disc,
    ShipMode=rng.choice(["Standard","Express","Same Day"],n,p=[.6,.3,.1]),
    PaymentMode=rng.choice(["UPI","Card","Cash on Delivery","Net Banking"],n,p=[.45,.25,.2,.1])))
sales = sales.sort_values("OrderDate").reset_index(drop=True)
sales["OrderID"] = [f"ORD{50001+i}" for i in range(len(sales))]

# ---------- Inject dirty data into RAW exports ----------
raw = sales.copy()
raw["OrderDate"] = raw["OrderDate"].dt.strftime("%d-%m-%Y")
raw["Quantity"] = raw["Quantity"].astype(object)
raw["Discount"] = raw["Discount"].astype(object)
idx = rng.choice(len(raw),30,replace=False); raw.loc[idx,"Quantity"] = np.nan          # missing qty
idx = rng.choice(len(raw),25,replace=False); raw.loc[idx,"ShipMode"] = np.nan          # missing ship mode
idx = rng.choice(len(raw),20,replace=False); raw.loc[idx,"PaymentMode"] = raw.loc[idx,"PaymentMode"].str.upper()  # inconsistent case
idx = rng.choice(len(raw),15,replace=False); raw.loc[idx,"Discount"] = raw.loc[idx,"Discount"].apply(lambda v: f"{int(v*100)}%")  # text %
raw = pd.concat([raw, raw.sample(40,random_state=1)]).sample(frac=1,random_state=2).sort_values("OrderID")   # 40 duplicate rows
raw["Remarks"] = ""            # unnecessary empty column
raw["Unnamed_Index"] = range(len(raw))   # unnecessary index column
raw.to_csv("data/raw_sales.csv", index=False)

rc = customers.copy()
rc["CustomerName"] = rc["CustomerName"].str.upper().where(rng.random(len(rc))<.3, rc["CustomerName"])
rc.loc[rng.choice(len(rc),6,replace=False),"Segment"] = np.nan
rc.to_csv("data/raw_customers.csv", index=False)
products.to_csv("data/raw_products.csv", index=False)
print(len(raw), "raw sales rows;", len(sales), "clean;", len(customers),"customers;", len(products),"products")
