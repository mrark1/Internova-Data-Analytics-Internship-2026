import pandas as pd, numpy as np, json
s = pd.read_csv("data/raw_sales.csv"); c = pd.read_csv("data/raw_customers.csv"); p = pd.read_csv("data/raw_products.csv")
log = {}
log["raw_rows"]=len(s); log["dup_rows"]=int(s.duplicated(subset="OrderID").sum())
log["null_qty"]=int(s.Quantity.isna().sum()); log["null_ship"]=int(s.ShipMode.isna().sum())
log["pct_text_discount"]=int(s.Discount.astype(str).str.contains("%").sum())
log["upper_pay"]=int((s.PaymentMode==s.PaymentMode.str.upper()).sum()-0)
log["null_segment"]=int(c.Segment.isna().sum())
# ---- clean (mirrors Power Query) ----
s = s.drop(columns=["Remarks","Unnamed_Index"]).drop_duplicates(subset="OrderID")
s = s.dropna(subset=["Quantity"])
s["Quantity"]=s.Quantity.astype(int)
s["Discount"]=s.Discount.astype(str).str.replace("%","",regex=False).astype(float)
s.loc[s.Discount>1,"Discount"]=s.Discount/100
s["ShipMode"]=s.ShipMode.fillna("Unknown")
pm = s.PaymentMode.str.title().replace({"Upi":"UPI"}); s["PaymentMode"]=pm
s["OrderDate"]=pd.to_datetime(s.OrderDate,format="%d-%m-%Y")
c["CustomerName"]=c.CustomerName.str.title(); c["Segment"]=c.Segment.fillna("Unknown")
log["clean_rows"]=len(s)
s.to_csv("data/clean_sales.csv",index=False); c.to_csv("data/clean_customers.csv",index=False); p.to_csv("data/clean_products.csv",index=False)
# ---- model ----
m = s.merge(p,on="ProductID",how="left").merge(c,on="CustomerID",how="left")
assert m.Category.notna().all() and m.Region.notna().all()
m["Sales"]=m.Quantity*m.UnitPrice*(1-m.Discount)
m["Cost"]=m.Quantity*m.UnitCost
m["Profit"]=m.Sales-m.Cost
m["Year"]=m.OrderDate.dt.year; m["MonthNo"]=m.OrderDate.dt.month; m["Month"]=m.OrderDate.dt.strftime("%b")
m["YM"]=m.OrderDate.dt.to_period("M").astype(str)
m.to_pickle("model.pkl")
k = dict(total_sales=m.Sales.sum(), total_profit=m.Profit.sum(), orders=len(m), units=int(m.Quantity.sum()),
         avg_order=m.Sales.mean(), max_order=m.Sales.max(), min_order=m.Sales.min(), margin=m.Profit.sum()/m.Sales.sum(),
         customers=m.CustomerID.nunique())
y = m.groupby("Year").Sales.sum(); k["sales_2024"]=y[2024]; k["sales_2025"]=y[2025]; k["yoy"]=y[2025]/y[2024]-1
print(json.dumps(log,indent=1)); print({a:round(float(b),3) for a,b in k.items()})
for col in ["Category","Region","Segment","PaymentMode","ShipMode"]:
    g=m.groupby(col).agg(Sales=("Sales","sum"),Profit=("Profit","sum"),Orders=("OrderID","count")); g["Margin"]=g.Profit/g.Sales; g["Share"]=g.Sales/g.Sales.sum()
    print("\n",g.sort_values("Sales",ascending=False).round(3))
print(m.groupby("ProductName").agg(Sales=("Sales","sum"),Profit=("Profit","sum")).sort_values("Sales",ascending=False).round(0))
mm=m.groupby("Month").Sales.sum(); print(mm.sort_values(ascending=False).round(0))
q=m.groupby(m.OrderDate.dt.quarter).Sales.sum(); print(q.round(0))
print(m.groupby("City").Sales.sum().sort_values(ascending=False).round(0).head(5))
dd=m.groupby(pd.cut(m.Discount,[-.01,0,.05,.10,.15,.20])).agg(Sales=("Sales","sum"),Profit=("Profit","sum"),n=("OrderID","count")); dd["Margin"]=dd.Profit/dd.Sales; print(dd.round(3))
json.dump({a:float(b) for a,b in k.items()},open("kpis.json","w")); json.dump(log,open("cleanlog.json","w"))
