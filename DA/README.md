# Data Analysis on Titanic Passenger Data

## Overview

This project is an exercise in data analysis using the Titanic dataset. The dataset contains detailed information about passengers aboard the Titanic. By analyzing this data, we aim to uncover patterns and insights related to survival rates. With Python’s powerful tools, we can progressively explore the data, apply different scopes or targets, and visually reflect trends for better understanding.

## Dataset Information

The Titanic dataset is provided in CSV format and includes the following columns:

1. **PassengerId** – Unique identifier for each passenger.
2. **Survived** – Survival status (0 = No, 1 = Yes).
3. **Pclass** – Passenger class (1st, 2nd, or 3rd).
4. **Name** – Full name of the passenger.
5. **Sex** – Gender of the passenger.
6. **Age** – Age of the passenger.
7. **SibSp** – Number of siblings/spouses aboard.
8. **Parch** – Number of parents/children aboard.
9. **Ticket** – Ticket number.
10. **Fare** – Fare paid for the ticket.
11. **Cabin** – Cabin number (if known).
12. **Embarked** – Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

---

## 1. Load and Explore the Data

- Imported the Titanic dataset into a Pandas DataFrame.
- Displayed the first few rows.
- Generated summary statistics to understand the structure of the dataset.
- **Data Cleaning**: Retained relevant columns such as **Survived**, **Sex**, **Age**, **Pclass**, **SibSp**, **Parch**, **Fare**, and **Embarked**, while removing those that were deemed insignificant for this study or had many null values.

## 2. Data Visualization

- **Histograms** to display distributions of key values.
- Grouped **Age** into categories and visualized using a **countplot** to show the distribution of passengers in each age group.
- **Pie charts** to represent **age distribution** and survival rates across different age groups.
- **Histograms** of passenger ages in 12 even bins to highlight skewness in age distribution.

## 3. Data Analysis and Interpretation

- **Survival rate analysis** by passenger class, gender, SibSp, Parch, and fare paid.
- **Gender-based survival analysis**: Women had a significantly higher survival rate compared to men.

## 4. Insights and Results

- **Survival Trends**: Clear patterns emerged showing that higher-class passengers, women, and those who paid higher fares were more likely to survive.
- **Family Dynamics**: Having family aboard had mixed effects, with passengers traveling alone or with fewer family members tending to have lower survival chances.
- **Gender Influence**: Female passengers had a significantly higher survival rate, aligning with historical rescue patterns on the Titanic.
- **Anomaly Detected**: An unusual trend was observed among 2nd class passengers with 3 SibSp. This could be further investigated.
- **Final Graph Insight**: The last graph strongly emphasizes that female passengers survived at a much higher rate than men—but not in all fare groups. The overlay shows the green point as the percentage of females in that group, while the bar represents the survival rate.

## Conclusion

Through this analysis, we uncovered data insights, visualized them in different ways, and explored various metrics to test theories. It was an engaging process that transformed raw data from a simple DataFrame into meaningful trends. With programming, we extracted valuable patterns that help us better understand what happened in this tragic event. These data-driven visualizations are powerful tools for analysis and storytelling.

---

## Technologies Used

- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## Extensions Used

- **markdownlint** – Because I really like a well-formatted Markdown README file.
