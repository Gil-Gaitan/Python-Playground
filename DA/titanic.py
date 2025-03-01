# Data Analysis on Titanic Passenger Data
# This project is an exercise in data analysis using the Titanic dataset.
# The dataset contains detailed information about passengers aboard the Titanic.
# By analyzing this data, we aim to uncover patterns and insights related to survival rates.

# Provided in CSV format:

# 1. **PassengerId** – Unique identifier for each passenger.
# 2. **Survived** – Survival status (0 = No, 1 = Yes).
# 3. **Pclass** – Passenger class (1st, 2nd, or 3rd).
# 4. **Name** – Full name of the passenger.
# 5. **Sex** – Gender of the passenger.
# 6. **Age** – Age of the passenger.
# 7. **SibSp** – Number of siblings/spouses aboard.
# 8. **Parch** – Number of parents/children aboard.
# 9. **Ticket** – Ticket number.
# 10. **Fare** – Fare paid for the ticket.
# 11. **Cabin** – Cabin number (if known).
# 12. **Embarked** – Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

# Step 1: Load and Explore the Data

# - Import the Titanic dataset into a Pandas DataFrame.
# - Display the first few rows and generate summary statistics.
# - Identify and handle any missing values appropriately.

# Step 2. Data Visualization

# - Create visualizations to explore key variables such as age, passenger class, gender, and fare.
# - Generate a **pie chart** to illustrate the survival distribution by age.
# - Use a **histogram** to analyze the age distribution of passengers.

# Step 3. Data Analysis and Interpretation

# - Examine the correlation between **passenger class** and **survival rate**.
# - Investigate the impact of **gender** on survival likelihood.
# - Analyze how the number of **siblings/spouses (SibSp)** and **parents/children (Parch)** aboard
#       affected survival chances.
# - Explore the relationship between **fare paid** and **survival probability**.

# Conclusions in data visualization.

# Through this analysis, we aim to gain insights into the factors that influenced passenger
#      survival rates on the Titanic. The findings from this project can help demonstrate the
#      power of data analysis in understanding real-world historical events.

# ---

# ### Technologies Used

# - **Python**
# - **Pandas**
# - **Matplotlib**
# - **Seaborn**

# For further improvements, additional machine learning techniques can be applied to predict
#     survival probabilities based on passenger attributes.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---
print("\n" + "-" * 145)
print("Data Analysis on Titanic Passenger Data")
print("-" * 145 + "\n")

# 1.a. Load the Titanic dataset into a Pandas DataFrame
file_path = "/Users/ggmacair2023/Desktop/Python Playgr/DA/titanic-2.csv"  # Change this to your file path
df = pd.read_csv(file_path)  # Load the dataset into a DataFrame

print("1.a. Titanic dataset is loaded into a Pandas DataFrame.")
print("-" * 55 + "\n\n")

# 1.b. Display the first few rows of the dataset and generate summary statistics
df_head = df.head()
df_summary = df.describe()
print("1.b. First few rows of the Titanic dataset and summary stats:")
print(("-" * 61) + "\n")
print(df_head)
print()
print(df_summary)
print("\n")

# 1.c. Identify and handle any missing values appropriately
missing_values = df.isnull().sum()
print("1.c. Missing values in the Titanic dataset:")
print("-" * 43 + "\n")
print(missing_values)
print("\n")

print("Data shape:  ", df.shape)
print("Dropping 'PassengerId' and 'Cabin' columns from the dataset.")
df.drop(["PassengerId", "Cabin"], axis=1, inplace=True)
print("Data shape after dropping columns:  ", df.shape)
print("\n")

# Print average fare
print("Average fare paid by passengers: ${:.2f}".format(df["Fare"].mean()))
print()

# Print average age
print("Average age of passengers: {:.2f}".format(df["Age"].mean()))
print("\n")

# Graph survival of all passengers
plt.figure(figsize=(10, 5))
sns.countplot(x="Survived", data=df)
plt.title("Not survived vs Survived")
plt.xlabel("Survival")
plt.ylabel("Count")
plt.show()

# Graph gender distribution
plt.figure(figsize=(10, 5))
df.Sex.value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90, colors=["skyblue", "lightgreen"]
)
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# Graph survival count
plt.figure(figsize=(10, 5))
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.xlabel("Survival")
plt.ylabel("Count")
plt.show()

# 2.a. Explore key variables: Age, Passenger Class, Gender, and Fare using visualizations
plt.figure(figsize=(15, 10))

# Histogram of Age
plt.subplot(2, 2, 1)
sns.histplot(df["Age"].dropna(), bins=30, kde=True)
plt.title("Distribution of Passenger Ages")

# Countplot of Passenger Class
plt.subplot(2, 2, 2)
sns.countplot(x="Pclass", data=df, palette="Set2")
plt.title("Passenger Class Distribution")

# Countplot of Gender
plt.subplot(2, 2, 3)
sns.countplot(x="Sex", data=df, palette="coolwarm")
plt.title("Gender Distribution")

# Distribution of Fare
plt.subplot(2, 2, 4)
sns.histplot(df["Fare"], bins=40, kde=True)
plt.title("Distribution of Fare Paid")

# Display the visualizations
plt.tight_layout()
plt.show()
