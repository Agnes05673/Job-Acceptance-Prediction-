print("Hello")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully")
import pandas as pd

# Load dataset
df = pd.read_csv("HR_Job_Placement_Dataset.csv")

# Display first 5 rows
print(df.head())
df = pd.read_csv("HR_Job_Placement_Dataset.csv")

import pandas as pd

# Load dataset
df = pd.read_csv("HR_Job_Placement_Dataset.csv")

# First 5 rows
print(df.head())

# Dataset shape
print(df.shape)

# Column names
print(df.columns)

# Data types
print(df.info())
# --------------------------------
# Standardize categorical values
# --------------------------------

df["gender"] = (
    df["gender"]
    .str.strip()
    .str.title()
)

df["company_tier"] = (
    df["company_tier"]
    .str.strip()
)

# Missing values
print(df.isnull().sum())
# Check duplicate rows
print("Duplicate Rows:", df.duplicated().sum())
# Fill numerical missing values with median

df["ssc_percentage"] = df["ssc_percentage"].fillna(df["ssc_percentage"].median())

df["hsc_percentage"] = df["hsc_percentage"].fillna(df["hsc_percentage"].median())

df["notice_period_days"] = df["notice_period_days"].fillna(df["notice_period_days"].median())

df["employment_gap_months"] = df["employment_gap_months"].fillna(df["employment_gap_months"].median())
# Fill categorical missing values with mode

df["career_switch_willingness"] = df["career_switch_willingness"].fillna(df["career_switch_willingness"].mode()[0])

df["relevant_experience"] = df["relevant_experience"].fillna(df["relevant_experience"].mode()[0])

df["job_role_match"] = df["job_role_match"].fillna(df["job_role_match"].mode()[0])

df["layoff_history"] = df["layoff_history"].fillna(df["layoff_history"].mode()[0])

df["relocation_willingness"] = df["relocation_willingness"].fillna(df["relocation_willingness"].mode()[0])
# Check missing values again
print(df.isnull().sum())
print(df["status"].unique())
print(df["gender"].unique())
print(df["company_tier"].unique())
# Save cleaned dataset
df.to_csv("cleaned_HR_Job_Placement_Dataset.csv", index=False)

print("Cleaned dataset saved successfully")

