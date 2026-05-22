
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("cleaned_HR_Job_Placement_Dataset.csv")
# --------------------------------
# Sidebar Filters
# --------------------------------

st.sidebar.header("Filter Options")

# Company Tier Filter

selected_company_tier = st.sidebar.multiselect(
    "Select Company Tier",
    options=df["company_tier"].unique(),
    default=df["company_tier"].unique()
)

# Gender Filter

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

# Apply Filters

filtered_df = df[
    (df["company_tier"].isin(selected_company_tier)) &
    (df["gender"].isin(selected_gender))
]

# --------------------------------
# Dashboard Title
# --------------------------------

st.title("Job Placement Analytics Dashboard")

st.subheader("Candidate Placement Analysis System")

# --------------------------------
# Dataset Preview
# --------------------------------

st.subheader("Dataset Preview")

st.dataframe(filtered_df.head())

# --------------------------------
# KPI Calculations
# --------------------------------

total_candidates = len(filtered_df)

placement_rate = (
    (filtered_df["status"] == "Placed").mean()
) * 100

average_interview_score = (
    filtered_df["communication_score"].mean()
)

average_skills_match = (
    filtered_df["skills_match_percentage"].mean()
)

# --------------------------------
# KPI Display
# --------------------------------

st.subheader("Key Performance Indicators")

col1, col2 = st.columns(2)

col1.metric(
    "Total Candidates",
    total_candidates
)

col2.metric(
    "Placement Rate (%)",
    round(placement_rate, 2)
)

col3, col4 = st.columns(2)

col3.metric(
    "Average Interview Score",
    round(average_interview_score, 2)
)

col4.metric(
    "Average Skills Match %",
    round(average_skills_match, 2)
)

# --------------------------------
# Placement Distribution
# --------------------------------

st.subheader("Placement Distribution")

fig, ax = plt.subplots()

sns.countplot(
    x="status",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# --------------------------------
# Company Tier vs Placement
# --------------------------------

st.subheader("Company Tier vs Placement")

fig, ax = plt.subplots(figsize=(8, 5))

sns.countplot(
    x="company_tier",
    hue="status",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# --------------------------------
# Experience vs Placement
# --------------------------------

st.subheader("Experience vs Placement")

fig, ax = plt.subplots(figsize=(8, 5))

sns.boxplot(
    x="status",
    y="years_of_experience",
    data=filtered_df,
    ax=ax
)

st.pyplot(fig)

# --------------------------------
# Skills Match Distribution
# --------------------------------

st.subheader("Skills Match Distribution")

fig, ax = plt.subplots(figsize=(8, 5))

sns.histplot(
    filtered_df["skills_match_percentage"],
    bins=20,
    ax=ax
)

st.pyplot(fig)
# --------------------------------
# High Risk Candidates KPI
# --------------------------------

high_risk_candidates = filtered_df[
    (filtered_df["communication_score"] < 50) |
    (filtered_df["skills_match_percentage"] < 50)
]

high_risk_percentage = (
    len(high_risk_candidates) / len(filtered_df)
) * 100

st.metric(
    "High Risk Candidate %",
    round(high_risk_percentage, 2)
)
