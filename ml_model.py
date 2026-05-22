import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Load cleaned dataset

df = pd.read_csv("cleaned_HR_Job_Placement_Dataset.csv")

print(df.head())
# Experience category feature

def experience_category(years):

    if years == 0:
        return "Fresher"

    elif years <= 3:
        return "Junior"

    else:
        return "Senior"

df["experience_category"] = df["years_of_experience"].apply(experience_category)

print(df[["years_of_experience", "experience_category"]].head())


# Academic performance bands

def academic_band(score):

    if score >= 75:
        return "Excellent"

    elif score >= 60:
        return "Good"

    else:
        return "Average"

df["academic_performance_band"] = df["degree_percentage"].apply(academic_band)

print(df[["degree_percentage", "academic_performance_band"]].head())
# Skills match level

def skills_level(score):

    if score >= 80:
        return "High"

    elif score >= 50:
        return "Medium"

    else:
        return "Low"

df["skills_match_level"] = df["skills_match_percentage"].apply(skills_level)

print(df[["skills_match_percentage", "skills_match_level"]].head())
# Interview performance category

def interview_category(score):

    if score >= 75:
        return "Strong"

    elif score >= 50:
        return "Moderate"

    else:
        return "Weak"

df["interview_performance_category"] = df["communication_score"].apply(interview_category)

print(df[["communication_score", "interview_performance_category"]].head())
# Placement probability score

df["placement_probability_score"] = (
    df["technical_score"] * 0.3 +
    df["aptitude_score"] * 0.2 +
    df["communication_score"] * 0.2 +
    df["skills_match_percentage"] * 0.3
)

print(df["placement_probability_score"].head())

#Encode target column

label_encoder = LabelEncoder()

df["status"] = label_encoder.fit_transform(df["status"])

print(df["status"].head())
# Encode categorical columns

categorical_columns = df.select_dtypes(include=['object']).columns

for column in categorical_columns:
    df[column] = label_encoder.fit_transform(df[column])

print("Categorical columns encoded successfully")
print(df.info()) 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix 
# Features and target

X = df.drop("status", axis=1)

y = df["status"]

print("Feature shape:", X.shape)

print("Target shape:", y.shape)

# Split dataset into training and testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data shape:", X_train.shape)

print("Testing data shape:", X_test.shape) 
# Train Logistic Regression model

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("Model trained successfully")
# Make predictions

y_pred = model.predict(X_test)

print("Predictions:")

print(y_pred[:10])
# Model accuracy

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy Score:", accuracy)
# Classification report

print(classification_report(y_test, y_pred)) 
# Confusion matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")

print(cm)