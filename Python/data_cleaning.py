import pandas as pd

df = pd.read_csv("D:\MCA\College Project\Dataset\Electronics.csv")

print(df.head())
print(df.shape)

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicates Removed")
print(df.shape)

numeric_cols = [
    "Quantity",
    "Unit_Price",
    "Unit_Cost",
    "Revenue",
    "Cost",
    "Profit",
    "Profit_Margin"
]

print(df[numeric_cols].describe())

print("Negative Revenue")
print((df["Revenue"] < 0).sum())

print("Negative Profit")
print((df["Profit"] < 0).sum())

print(df["Age"].describe())

outliers = df[
    (df["Age"] < 18) |
    (df["Age"] > 80)
]

print(outliers.shape)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Check column names
print(df.columns.tolist())

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

# Verify conversion
print(df["Order_Date"].dtype)

# Check failed conversions
print(df["Order_Date"].isna().sum())

# Create new columns
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month_name()
df["Quarter"] = df["Order_Date"].dt.quarter

df["Year"] = df["Order_Date"].dt.year


df["Revenue_Category"] = pd.cut(
    df["Revenue"],
    bins=[0,50000,150000,300000,1000000],
    labels=["Low","Medium","High","Premium"]
)

print(df.columns.tolist())

print("\nRevenue Summary")
print(df["Revenue"].describe())

print("\nProfit Summary")
print(df["Profit"].describe())

top_brands = (
    df.groupby("Brand")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_brands)

top_products = (
    df.groupby("Product_Name")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)

region_sales = (
    df.groupby("Region")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(region_sales)

segment_sales = (
    df.groupby("Customer_Segment")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(segment_sales)

membership_sales = (
    df.groupby("Membership_Type")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(membership_sales)

year_sales = (
    df.groupby("Year")["Revenue"]
      .sum()
      .sort_index()
)

print(year_sales)

negative_profit = df[df["Profit"] < 0]

print(negative_profit[
    ["Product_Name","Brand","Revenue","Cost","Profit"]
].head(20))

print("\n========== DATA QUALITY REPORT ==========")

print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))
print("Duplicate Records:", df.duplicated().sum())
print("Missing Values:", df.isnull().sum().sum())
print("Unique Customers:", df["Customer_ID"].nunique())
print("Unique Products:", df["Product_Name"].nunique())

print("\nNegative Revenue Records:")
print((df["Revenue"] < 0).sum())

print("\nNegative Profit Records:")
print((df["Profit"] < 0).sum())

print("\nReturned Orders:")
print((df["Order_Status"] == "Returned").sum())

print("\nCancelled Orders:")
print((df["Order_Status"] == "Cancelled").sum())

print("\n=========================================")

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()

print("Total Revenue:", round(total_revenue,2))
print("Total Profit:", round(total_profit,2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)

category_map = {
    "Smart TV":"Entertainment",
    "OLED TV":"Entertainment",
    "Soundbar":"Entertainment",
    "Gaming Console":"Entertainment",

    "iPhone":"Mobile Devices",
    "Galaxy Phone":"Mobile Devices",
    "OnePlus Phone":"Mobile Devices",
    "Smart Watch":"Mobile Devices",
    "Earbuds":"Mobile Devices",

    "Laptop":"Computing",
    "MacBook":"Computing",
    "Tablet":"Computing",
    "iPad":"Computing",
    "Monitor":"Computing",
    "Printer":"Computing",

    "Refrigerator":"Home Appliances",
    "Washing Machine":"Home Appliances",
    "Air Conditioner":"Home Appliances",
    "Water Purifier":"Home Appliances",

    "Air Fryer":"Kitchen Appliances",
    "Microwave":"Kitchen Appliances",
    "Vacuum Cleaner":"Home Appliances",
    "Bluetooth Speaker":"Entertainment"
}

df["Category"] = df["Product_Name"].map(category_map)