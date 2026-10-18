// ============================================================
// Week 5 - Power BI | Power Query (M) scripts
// Paste each block into  Home > Transform data > (new blank query) > Advanced Editor
// Change the folder path to where you saved the CSV files.
// ============================================================

// ---------- Query 1 : Sales ----------
let
    Source      = Csv.Document(File.Contents("C:\PowerBI_Week5\data\raw_sales.csv"),
                    [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted    = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),

    // 1. remove unnecessary columns
    DropCols    = Table.RemoveColumns(Promoted, {"Remarks", "Unnamed_Index"}),

    // 2. remove the 40 duplicate orders
    NoDuplicates= Table.Distinct(DropCols, {"OrderID"}),

    // 3. drop the 30 rows that have no Quantity
    NoBlankQty  = Table.SelectRows(NoDuplicates,
                    each [Quantity] <> null and [Quantity] <> ""),

    // 4. Discount: text such as "15%" -> number 0.15
    FixDiscount = Table.TransformColumns(NoBlankQty, {{"Discount",
                    each if Text.Contains(_, "%")
                         then Number.FromText(Text.Replace(_, "%", ""), "en-US") / 100
                         else Number.FromText(_, "en-US"), type number}}),

    // 5. missing ShipMode -> "Unknown"
    FixShip     = Table.TransformColumns(FixDiscount, {{"ShipMode",
                    each if _ = null or _ = "" then "Unknown" else _, type text}}),

    // 6. consistent casing in PaymentMode (UPI stays upper case)
    FixPayment  = Table.TransformColumns(FixShip, {{"PaymentMode",
                    each if Text.Upper(_) = "UPI" then "UPI" else Text.Proper(_), type text}}),

    // 7. OrderDate text (dd-mm-yyyy) -> Date, Quantity -> whole number
    Typed       = Table.TransformColumnTypes(FixPayment,
                    {{"OrderDate", type date}, {"Quantity", Int64.Type}}, "en-GB"),
    Typed2      = Table.TransformColumnTypes(Typed,
                    {{"OrderID", type text}, {"CustomerID", type text}, {"ProductID", type text}})
in
    Typed2

// ---------- Query 2 : Customers ----------
let
    Source   = Csv.Document(File.Contents("C:\PowerBI_Week5\data\raw_customers.csv"),
                 [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Proper   = Table.TransformColumns(Promoted, {{"CustomerName", Text.Proper, type text}}),
    Segment  = Table.TransformColumns(Proper, {{"Segment", each if _ = null or _ = "" then "Unknown" else _, type text}}),
    Typed    = Table.TransformColumnTypes(Segment, {{"CustomerID", type text}, {"Region", type text}, {"City", type text}})
in
    Typed

// ---------- Query 3 : Products ----------
let
    Source   = Csv.Document(File.Contents("C:\PowerBI_Week5\data\raw_products.csv"),
                 [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed    = Table.TransformColumnTypes(Promoted,
                 {{"ProductID", type text}, {"ProductName", type text}, {"Category", type text},
                  {"UnitPrice", Currency.Type}, {"UnitCost", Currency.Type}}, "en-US")
in
    Typed
