from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the breast cancer dataset into a pandas
data = load_breast_cancer()

X = data.data  # Features
y = data.target  # Labels

print(
    "\n\nSection 1 - Part A: Load the breast cancer dataset into a pandas DataFrame\n"
)

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

# Display the first 5 samples
print("First 5 Samples:")
print(df.head())
print("\n")

# Split the dataset into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print("Data successfully split into training (70%) and testing (30%).\n")

# Initialize Gaussian Naïve Bayes model
model = GaussianNB()
print("Gaussian Naïve Bayes model initialized.\n")

# Train the model
model.fit(X_train, y_train)
print("Model training complete.\n")

# Display the model parameters
print("Model Parameters:")
print(f"Classes: {model.classes_}")
print(f"Class Priors: {model.class_prior_}")
print(f"Class Count: {model.class_count_}")

# Make predictions
y_pred = model.predict(X_test)
print("Predictions made on the test set.\n")

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Gaussian Naïve Bayes: {accuracy:.4f}\n")

# Additional performance metrics
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix visualization
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=data.target_names,
    yticklabels=data.target_names,
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Cool Feature: Calculate and display feature importance based on standard deviations
feature_importance = np.std(X_train, axis=0)
important_features = np.argsort(feature_importance)[-5:][
    ::-1
]  # Top 5 important features

print("Top 5 Most Important Features (based on standard deviation):")
for i, idx in enumerate(important_features):
    print(f"{i+1}. {data.feature_names[idx]} (Std Dev: {feature_importance[idx]:.4f})")

# Run the model again using 15% from one side of the dataset and 15% from the other
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(
    X, y, test_size=0.3, random_state=42, shuffle=False
)
print("Running second split: 15% from one side and 15% from the other.\n")

# Train a new Gaussian Naïve Bayes model on the new split
model_2 = GaussianNB()
model_2.fit(X_train_2, y_train_2)
y_pred_2 = model_2.predict(X_test_2)

# Calculate new accuracy
accuracy_2 = accuracy_score(y_test_2, y_pred_2)
print(f"Accuracy of Gaussian Naïve Bayes on second split: {accuracy_2:.4f}\n")

# Display second confusion matrix
conf_matrix_2 = confusion_matrix(y_test_2, y_pred_2)
plt.figure(figsize=(6, 4))
sns.heatmap(
    conf_matrix_2,
    annot=True,
    fmt="d",
    cmap="Reds",
    xticklabels=data.target_names,
    yticklabels=data.target_names,
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Second Split")
plt.show()


#
