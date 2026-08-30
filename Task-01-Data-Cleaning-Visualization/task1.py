import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("house_data.csv")

print("\n----- ORIGINAL DATA -----")
print(df)

print("\n----- DATA INFORMATION -----")
df.info()

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

print("\n----- DUPLICATE ROWS -----")
print(df.duplicated().sum())

df = df.drop_duplicates()

df.to_csv("cleaned_house_data.csv", index=False)
print("\nCleaned dataset saved successfully!")

print("\n----- STATISTICAL SUMMARY -----")
print(df.describe())

plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10)
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Houses")
plt.savefig("outputs/house_price_distribution.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df["Bedrooms"], df["Price"])
plt.title("Bedrooms vs Price")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Price")
plt.savefig("outputs/bedrooms_vs_price.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Price"])
plt.title("Price Box Plot")
plt.savefig("outputs/price_boxplot.png")
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")
plt.show()

print("\nTask 01 completed successfully!")