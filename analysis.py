import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("📊 Welcome to Sales Data Analysis")

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------
try:
    df = pd.read_csv("sales.csv")
    print("✅ Dataset Loaded Successfully\n")
    print("First 5 rows:\n", df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:\n", df.isnull().sum())

    # Fill missing values if any
    df.fillna(df.mean(numeric_only=True), inplace=True)

except FileNotFoundError:
    print("❌ sales.csv not found. Please place it in the project folder.")
    exit()

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------
print("\n📈 Basic Statistics:\n", df.describe())

grouped_sales = df.groupby("Region")["Sales"].mean()
print("\nAverage Sales per Region:\n", grouped_sales)

# -------------------------------
# Task 3: Data Visualization
# -------------------------------
plt.style.use("seaborn")

# 1. Line Chart - Sales Trend Over Time
plt.figure(figsize=(8,5))
plt.plot(df["Date"], df["Sales"], marker="o", color="b")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average Sales per Region
plt.figure(figsize=(6,4))
sns.barplot(x="Region", y="Sales", data=df, ci=None, palette="viridis")
plt.title("Average Sales by Region")
plt.xlabel("Region")
plt.ylabel("Average Sales")
plt.show()

# 3. Histogram - Profit Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Profit"], bins=10, color="orange", edgecolor="black")
plt.title("Distribution of Profit")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Sales vs Profit
plt.figure(figsize=(6,5))
sns.scatterplot(x="Sales", y="Profit", hue="Region", data=df, palette="deep")
plt.title("Sales vs Profit by Region")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.legend(title="Region")
plt.show()
