# ============================================================
# DATA CLEANING & STRUCTURAL VALIDATION
# Internship Task - Data Analytics
# ============================================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("="*60)
print("DATA CLEANING & STRUCTURAL VALIDATION")
print("="*60)

# ------------------------------------------------------------
# STEP 1 : Create Sample Raw Dataset
# (Replace this with pd.read_csv("your_dataset.csv") if needed)
# ------------------------------------------------------------

data = {
    "Name": ["Alice", "Bob", "Alice", "David", np.nan, "Emily", "Bob"],
    "Age": [25, 30, 25, np.nan, 28, 22, 30],
    "Gender": ["Female", "Male", "Female", "Male", "Female", None, "Male"],
    "Salary": [50000, 60000, 50000, 70000, 65000, 55000, 60000],
    "City": ["Hyderabad", "Delhi", "Hyderabad", "Mumbai", "Chennai", "Delhi", "Delhi"]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset")
print(df)

# ------------------------------------------------------------
# STEP 2 : Dataset Information
# ------------------------------------------------------------

print("\nDataset Information")
print(df.info())

print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ------------------------------------------------------------
# STEP 3 : Remove Duplicate Rows
# ------------------------------------------------------------

df = df.drop_duplicates()

print("\nDuplicate Rows Removed")

# ------------------------------------------------------------
# STEP 4 : Handle Missing Values
# ------------------------------------------------------------

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing gender
df["Gender"] = df["Gender"].fillna("Not Specified")

print("\nMissing Values Filled")

# ------------------------------------------------------------
# STEP 5 : Standardize Text
# ------------------------------------------------------------

df["Name"] = df["Name"].str.title()
df["Gender"] = df["Gender"].str.title()
df["City"] = df["City"].str.title()

# ------------------------------------------------------------
# STEP 6 : Correct Data Types
# ------------------------------------------------------------

df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(float)

# ------------------------------------------------------------
# STEP 7 : Validation
# ------------------------------------------------------------

print("\nValidation Results")

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:", df.duplicated().sum())

print("\nData Types")
print(df.dtypes)

# ------------------------------------------------------------
# STEP 8 : Summary Statistics
# ------------------------------------------------------------

print("\nSummary Statistics")
print(df.describe())

# ------------------------------------------------------------
# STEP 9 : Final Clean Dataset
# ------------------------------------------------------------

print("\nCleaned Dataset")
print(df)

# ------------------------------------------------------------
# STEP 10 : Save Clean Dataset
# ------------------------------------------------------------

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_dataset.csv'")

# ------------------------------------------------------------
# STEP 11 : Visualization
# ------------------------------------------------------------

plt.figure(figsize=(6,4))
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
df["City"].value_counts().plot(kind="bar")
plt.title("Employees by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

print("\nTask Completed Successfully!")
