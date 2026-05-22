import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_HR_Job_Placement_Dataset.csv")

# Set plot style
sns.set_style("whitegrid")

print("Dataset loaded successfully")
# Placement status distribution

sns.countplot(x="status", data=df)

plt.title("Placement Status Distribution")

plt.xlabel("Placement Status")

plt.ylabel("Candidate Count")

# Save graph
plt.savefig("placement_status_distribution.png")

print("Placement graph saved")

plt.clf()
# Communication score vs placement

sns.boxplot(x="status", y="communication_score", data=df)

plt.title("Communication Score vs Placement")

plt.xlabel("Placement Status")

plt.ylabel("Communication Score")

# Save graph
plt.savefig("communication_score_vs_placement.png")

print("Communication graph saved")

plt.clf()
# Skills match percentage vs placement

sns.boxplot(x="status", y="skills_match_percentage", data=df)

plt.title("Skills Match Percentage vs Placement")

plt.xlabel("Placement Status")

plt.ylabel("Skills Match Percentage")

# Save graph
plt.savefig("skills_match_vs_placement.png")

print("Skills graph saved")

plt.clf()
# Experience vs placement

sns.boxplot(x="status", y="years_of_experience", data=df)

plt.title("Years of Experience vs Placement")

plt.xlabel("Placement Status")

plt.ylabel("Years of Experience")

# Save graph
plt.savefig("experience_vs_placement.png")

print("Experience graph saved")

plt.clf()
# Company tier vs placement

sns.countplot(x="company_tier", hue="status", data=df)

plt.title("Company Tier vs Placement")

plt.xlabel("Company Tier")

plt.ylabel("Candidate Count")

# Save graph
plt.savefig("company_tier_vs_placement.png")

print("Company tier graph saved")

plt.clf()
# Correlation heatmap

numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation = numeric_df.corr()

plt.figure(figsize=(14,10))

sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")

# Save graph
plt.savefig("correlation_heatmap.png")

print("Heatmap saved")

plt.clf()