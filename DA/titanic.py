import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("\n" + "-" * 100)
print("Data Analysis on Titanic Passenger Data")
print("-" * 100 + "\n")

# 1.a. Load the Titanic dataset into a Pandas DataFrame
file_path = "/Users/ggmacair2023/Desktop/python-playground/DA/titanic-2.csv"  # Change this to your file path
df = pd.read_csv(file_path)  # Load the dataset into a DataFrame
print("Section 1 - Data Exploration")
print("-" * 100 + "\n\n")
print(
    "Task 1.a.\n" + ("-" * 9) + "\nTitanic dataset is loaded into a Pandas DataFrame.\n"
)

# 1.b. Display the first few rows of the dataset and generate summary statistics
print("Task 1.b.\n" + ("-" * 9))
print("Display first few rows of the dataset:")
print(df.head())

print("\nShape of this dataset (rows, columns): ", df.shape)

print("\nSummary statistics of the dataset:")
print(df.describe().round(2))
print("")

# Basic metrics of the dataset
print("Basic metrics of the dataset:")
print("Number of passengers:\t", df.shape[0])
print("Number of columns:\t", df.shape[1])
print("Header: ", df.columns.tolist())
print("")


# 1.c. Identify and handle any missing values appropriately
print("Task 1.c.\n" + ("-" * 9))
print("Identify and handle any missing values in the Titanic dataset:")
missing_values = df.isnull().sum()
print("\nIdentified null values.\n")
missing_columns = missing_values[missing_values > 0]
print("Display columns with missing values, and how many there are:")
print(missing_columns)
print("")
print("We need age, and only missing 2 Embarked is okay. We can drop Cabin.")
print("While we are cleaning the dataset, we can remove insignificant columns.")
df.drop(["PassengerId", "Cabin", "Ticket"], axis=1, inplace=True)
print("Data shape after dropping columns:  ", df.shape)
print("Removed PassengerId, Cabin, and Ticket columns.\n")

# Section 2
# 2.a. Data Visualization
print("Section 2 - Data Visualization")
print("-" * 100 + "\n\n")

# Explore distribution of key variables: Age, Pclass, gender, and Fare using visualizations
print("Task 2.a.\n" + ("-" * 9))
print("Displaying distribution of key statistics using visualizations.\n")

# Gender distribution
plt.figure(figsize=(10, 5))
df.Sex.value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90, colors=["skyblue", "lightgreen"]
)
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# Passenger class distribution
plt.figure(figsize=(10, 5))
sns.countplot(x="Pclass", data=df, hue="Pclass", palette="Set2", legend=False)
plt.title("Passenger Class Distribution")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()

# Age distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["Age"].dropna(), bins=30, kde=True)
plt.title("Distribution of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Age groups distribution, grouped by 0-12, 13-18, 19-30, 31-50, 51-80
plt.figure(figsize=(10, 5))
age_bins = [0, 12, 18, 30, 50, 80]
age_labels = ["0-12", "13-18", "19-30", "31-50", "51-80"]
df["AgeGroup"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)
sns.countplot(x="AgeGroup", data=df, palette="Set3")
plt.title("Age Groups Distribution")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()

# Fare distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["Fare"], bins=40, kde=True)
plt.title("Distribution of Fare Paid")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()

# 2 - b. Pie Charts that shows Age Distribution of survivors and non survivors
print("Task 2.b.\n" + ("-" * 9))
print("Displaying Age Distribution of survivors and non-survivors.\n")

# show a plain pie chart with passengers in each age group
plt.figure(figsize=(10, 5))
df["AgeGroup"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set3")
)
plt.title("All Passengers Age Distribution")
plt.ylabel("")
plt.show()

# Pie of Age Distribution of survivors
plt.figure(figsize=(10, 5))
df_survived = df[df["Survived"] == 1]
df_survived["AgeGroup"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set3")
)
plt.title("Age Distribution of Survivors")
plt.ylabel("")
plt.show()

# Pie of Age Distribution of non-survivors
plt.figure(figsize=(10, 5))
df_not_survived = df[df["Survived"] == 0]
df_not_survived["AgeGroup"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set3")
)
plt.title("Age Distribution of Non-Survivors")
plt.ylabel("")
plt.show()

print("Task 2.c.\n" + ("-" * 9))
print("Display Histogram of Age Distribution.\n")

# 2.c. Histogram of Age Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["Age"].dropna(), bins=12, kde=True)
plt.title("Histogram of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Section 3 - Data Analysis and Interpretation

# 3.a. Correlation between passenger class and survival rate?

# Calculate survival rate by passenger class
survival_by_class = df.groupby("Pclass", observed=False)["Survived"].mean().round(2)
print("\nSurvival rate by Passenger Class:")
print(survival_by_class)

# Plot survival rate by Passenger Class
plt.figure(figsize=(8, 5))
sns.barplot(x=survival_by_class.index, y=survival_by_class.values, palette="Blues_d")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

# 3.b. Correlation between gender and survival rate?
# Calculate survival rate by gender
survival_by_gender = df.groupby("Sex", observed=False)["Survived"].mean().round(2)
print("\nSurvival rate by Gender:")
print(survival_by_gender)

# Plot survival rate by Gender
plt.figure(figsize=(8, 5))
sns.barplot(x=survival_by_gender.index, y=survival_by_gender.values, palette="Set2")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.show()

# Print number of males that survived
male_survived = df[(df["Sex"] == "male") & (df["Survived"] == 1)]
print(f"\nNumber of males that survived: {male_survived.shape[0]}")

# 3.c.1. Correlation between number of siblings/spouses (SibSp) and survival rate?
# Calculate survival rate by SibSp (number of siblings/spouses aboard)
survival_by_sibsp = df.groupby("SibSp", observed=False)["Survived"].mean().round(2)
print("\nSurvival rate by SibSp (Siblings/Spouses aboard):")
print(survival_by_sibsp)

# Plot survival rate by SibSp
plt.figure(figsize=(10, 6))
sns.barplot(x=survival_by_sibsp.index, y=survival_by_sibsp.values)
plt.title("Survival Rate by Number of Siblings/Spouses (SibSp)")
plt.xlabel("Number of Siblings/Spouses (SibSp)")
plt.ylabel("Survival Rate")
plt.show()

# Plot survival rate by SibSp with hue for passenger class (Pclass)
plt.figure(figsize=(10, 6))
sns.barplot(x="SibSp", y="Survived", data=df, hue="Pclass", palette="viridis", ci=None)
plt.title("Survival Rate by Number of Siblings/Spouses (SibSp) and Passenger Class")
plt.xlabel("Number of Siblings/Spouses (SibSp)")
plt.ylabel("Survival Rate")
plt.show()


# 3.c.2. Correlation between number of parents/children (Parch) and survival rate?

# Calculate survival rate by Parch (number of parents/children aboard)
survival_by_parch = df.groupby("Parch", observed=False)["Survived"].mean().round(2)
print("\nSurvival rate by Parch (Parents/Children aboard):")
print(survival_by_parch)

# Plot survival rate by Parch
plt.figure(figsize=(10, 6))
sns.barplot(x=survival_by_parch.index, y=survival_by_parch.values)
plt.title("Survival Rate by Number of Parents/Children (Parch)")
plt.xlabel("Number of Parents/Children (Parch)")
plt.ylabel("Survival Rate")
plt.show()

# 3.d. Correlation between fare paid and survival rate?

# 3.d. Correlation between fare paid and survival rate (grouping fares into bins)

# Define fare bins and corresponding labels
fare_bins = [0, 10, 30, 50, 100, 200, 500]  # Adjust these ranges as necessary
fare_labels = ["0-10", "10-30", "30-50", "50-100", "100-200", "200+"]

# Create a new column in the DataFrame that categorizes fares into the defined bins
df["FareGroup"] = pd.cut(df["Fare"], bins=fare_bins, labels=fare_labels, right=False)

# Calculate the survival rate for each fare group
survival_by_fare_group = (
    df.groupby("FareGroup", observed=False)["Survived"].mean().round(2)
)

# Print survival rate by fare group
print("\nSurvival rate by Fare Group:")
print(survival_by_fare_group)

# Plot survival rate by fare group
plt.figure(figsize=(10, 6))
sns.barplot(
    x=survival_by_fare_group.index, y=survival_by_fare_group.values, palette="coolwarm"
)
plt.title("Survival Rate by Fare Paid (Grouped)")
plt.xlabel("Fare Group")
plt.ylabel("Survival Rate")
plt.show()

# 3.d. Correlation between fare paid, survival rate, and percentage of females

# Calculate the percentage of females and survival rate for each fare group
fare_group_stats = (
    df.groupby("FareGroup", observed=False)
    .agg(
        survival_rate=("Survived", "mean"),
        percentage_females=("Sex", lambda x: (x == "female").mean() * 100),
    )
    .round(2)
)

# Display the results
print("\nSurvival Rate and Percentage of Females by Fare Group:")
print(fare_group_stats)

# Plot survival rate and percentage of females by fare group in separate subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Survival Rate
sns.barplot(
    x=fare_group_stats.index,
    y=fare_group_stats["survival_rate"],
    ax=ax1,
    palette="coolwarm",
)
ax1.set_title("Survival Rate and Percentage of Females by Fare Group")
ax1.set_xlabel("Fare Group")
ax1.set_ylabel("Survival Rate", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Create a second axis to plot the percentage of females
ax2 = ax1.twinx()
sns.lineplot(
    x=fare_group_stats.index,
    y=fare_group_stats["percentage_females"],
    ax=ax2,
    color="green",
    marker="o",
)
ax2.set_ylabel("Percentage of Females", color="green")
ax2.tick_params(axis="y", labelcolor="green")

plt.tight_layout()
plt.show()
