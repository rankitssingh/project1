import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset load करें
df = pd.read_csv("sales_data.csv")

# 2. Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# 3. Quick overview
print("\n🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Statistics:")
print(df.describe())

# 4. Region-wise Sales
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\n🔹 Region-wise Sales:")
print(region_sales)

# Visualization - Region Sales
plt.figure(figsize=(8, 5))
sns.barplot(x=region_sales.index, y=region_sales.values,
            hue=region_sales.index, palette="viridis", legend=False)
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Monthly Sales Trend
df['Date'] = pd.to_datetime(df['Date'])  # ✅ 'Date' column use करें
monthly_sales = df.groupby(df['Date'].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o", color="blue")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Product-wise Sales
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\n🔹 Product-wise Sales:")
print(product_sales)

plt.figure(figsize=(8, 5))
sns.barplot(x=product_sales.index, y=product_sales.values,
            hue=product_sales.index, palette="coolwarm", legend=False)
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 7. Quantity vs Sales Scatter Plot
plt.figure(figsize=(7, 5))
sns.scatterplot(x="Quantity", y="Sales", data=df, hue="Product", palette="Set2")
plt.title("Quantity vs Sales (by Product)")
plt.xlabel("Quantity Sold")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
