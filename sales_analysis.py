import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("supermarket_large_dataset.csv")

# Sales Revenue by Product Category
category_sales = df.groupby("product_category")["sales_revenue"].sum()

category_sales = category_sales.sort_values(ascending=False)

print("Sales Revenue by Category:")
print(category_sales)

# Create Bar Chart
category_sales.plot(kind="bar")

plt.title("Supermarket Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
print("\n===== SALES ANALYSIS SUMMARY =====")

print("Total Number of Records:", len(df))
print("Total Sales Revenue:", round(df["sales_revenue"].sum(), 2))
print("Total Units Sold:", df["units_sold"].sum())

print("\n===== TOP 5 SALES RECORDS =====")
print(df.nlargest(5, "sales_revenue")[["sales_revenue", "units_sold"]])
print("\n===== DATASET INFORMATION =====")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Records:")
print(df.head())
# Remove duplicate rows
df = df.drop_duplicates()

print("\n===== DATA CLEANING =====")
print("Dataset cleaned successfully!")
print("Rows after removing duplicates:", len(df))
print("Missing values:", df.isnull().sum().sum())
# Check missing values in each column
print("\n===== MISSING VALUE ANALYSIS =====")

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])
# Professional Sales Analysis

print("\n===== PROFESSIONAL SALES ANALYSIS =====")

total_revenue = df["sales_revenue"].sum()
total_units = df["units_sold"].sum()

print("Total Sales Revenue:", round(total_revenue, 2))
print("Total Units Sold:", total_units)

if "profit_per_unit" in df.columns:
    total_profit = (df["profit_per_unit"] * df["units_sold"]).sum()
    print("Estimated Total Profit:", round(total_profit, 2))
    # Best Selling Products Analysis

print("\n===== TOP 10 SALES RECORDS =====")

top_sales = df.nlargest(10, "sales_revenue")

print(top_sales[["sales_revenue", "units_sold"]])
# Export Analysis Results

summary = pd.DataFrame({
    "Metric": ["Total Sales Revenue", "Total Units Sold"],
    "Value": [
        df["sales_revenue"].sum(),
        df["units_sold"].sum()
    ]
})

summary.to_csv("sales_summary.csv", index=False)

print("\nAnalysis results saved to sales_summary.csv")
# ===== ADDITIONAL SALES ANALYSIS =====

print("\n===== SALES REVENUE ANALYSIS =====")

print("Average Sales Revenue:",
      round(df["sales_revenue"].mean(), 2))

print("Highest Sales Revenue:",
      round(df["sales_revenue"].max(), 2))

print("Lowest Sales Revenue:",
      round(df["sales_revenue"].min(), 2))

print("\n===== UNITS SOLD ANALYSIS =====")

print("Average Units Sold:",
      round(df["units_sold"].mean(), 2))

print("Maximum Units Sold:",
      df["units_sold"].max())

print("Minimum Units Sold:",
      df["units_sold"].min())

print("\nAdditional analysis completed successfully!")
# ===== SALES REVENUE CHART =====

import matplotlib.pyplot as plt

print("\nCreating Sales Revenue Chart...")

plt.figure(figsize=(10, 6))

plt.hist(
    df["sales_revenue"].dropna(),
    bins=20,
    edgecolor="black"
)

plt.title("Supermarket Sales Revenue Distribution")
plt.xlabel("Sales Revenue")
plt.ylabel("Number of Records")

plt.tight_layout()
plt.savefig("sales_revenue_chart.png")

print("Chart saved as sales_revenue_chart.png")

plt.show()