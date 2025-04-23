import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- Load and structure the data ---
data = {
    "Referrer": [
        "slashdot",
        "google",
        "digg",
        "kiwitobes",
        "google",
        "(direct)",
        "(direct)",
        "google",
        "slashdot",
        "digg",
        "google",
        "kiwitobes",
        "digg",
        "google",
        "kiwitobes",
    ],
    "Location": [
        "USA",
        "France",
        "USA",
        "France",
        "UK",
        "New Zealand",
        "UK",
        "USA",
        "France",
        "USA",
        "UK",
        "UK",
        "New Zealand",
        "UK",
        "France",
    ],
    "Read FAQ": [
        "yes",
        "yes",
        "yes",
        "yes",
        "no",
        "no",
        "no",
        "no",
        "yes",
        "no",
        "no",
        "no",
        "yes",
        "yes",
        "yes",
    ],
    "Pages viewed": [18, 23, 24, 23, 21, 12, 21, 24, 19, 18, 18, 19, 12, 18, 19],
    "Service Chosen": [
        "None",
        "Premium",
        "Basic",
        "Basic",
        "Premium",
        "None",
        "Basic",
        "Premium",
        "None",
        "None",
        "None",
        "None",
        "Basic",
        "Basic",
        "Basic",
    ],
}

df = pd.DataFrame(data)

# --- Encode categorical features ---
df_encoded = df.copy()
label_encoders = {}

for column in ["Referrer", "Location", "Read FAQ", "Service Chosen"]:
    le = LabelEncoder()
    df_encoded[column] = le.fit_transform(df_encoded[column])
    label_encoders[column] = le

# Split features and target
X = df_encoded.drop("Service Chosen", axis=1)
y = df_encoded["Service Chosen"]

# --- Split data into training and testing sets ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# --- Train a decision tree classifier ---
classification = DecisionTreeClassifier(
    criterion="entropy", max_depth=4, random_state=42
)
classification.fit(X_train, y_train)

# --- Predict a single sample user ---
sample_user = pd.DataFrame(
    [
        {
            "Referrer": label_encoders["Referrer"].transform(["(direct)"])[0],
            "Location": label_encoders["Location"].transform(["USA"])[0],
            "Read FAQ": label_encoders["Read FAQ"].transform(["yes"])[0],
            "Pages viewed": 5,
        }
    ]
)

prediction = classification.predict(sample_user)
predicted_service = label_encoders["Service Chosen"].inverse_transform(prediction)
print("Predicted service for sample user:", predicted_service[0])

# Another prediction example
sample_user2 = pd.DataFrame(
    [
        {
            "Referrer": label_encoders["Referrer"].transform(["google"])[0],
            "Location": label_encoders["Location"].transform(["UK"])[0],
            "Read FAQ": label_encoders["Read FAQ"].transform(["no"])[0],
            "Pages viewed": 20,
        }
    ]
)
print(
    "Another prediction:",
    label_encoders["Service Chosen"].inverse_transform(
        classification.predict(sample_user2)
    )[0],
)

# --- Evaluate accuracy ---
y_pred = classification.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Decision Tree Accuracy:", round(acc * 100, 2), "%")

# --- Visualization ---

# 3. Large rounded version
plt.figure(figsize=(16, 8))
plot_tree(
    classification,
    filled=True,
    feature_names=X.columns,
    class_names=label_encoders["Service Chosen"].classes_,
    rounded=True,
)
plt.title("Decision Tree (Rounded & Large)")
plt.show()

# 4. Text output of tree
print("\nText representation of the decision tree:\n")
print(export_text(classification, feature_names=list(X.columns)))

# --- Train a Random Forest for comparison ---
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)
y_rf_pred = rf_clf.predict(X_test)
rf_accuracy = accuracy_score(y_test, y_rf_pred)
print("Random Forest Accuracy:", round(rf_accuracy * 100, 2), "%")

# --- Hyperparameter tuning for Decision Tree ---
param_grid = {
    "criterion": ["gini", "entropy"],
    "max_depth": [2, 3, 4, 5, None],
    "min_samples_split": [2, 3, 4],
    "min_samples_leaf": [1, 2, 3],
}

grid_search = GridSearchCV(
    DecisionTreeClassifier(random_state=42), param_grid, cv=3, scoring="accuracy"
)
grid_search.fit(X_train, y_train)

# Best estimator results
best_dt = grid_search.best_estimator_
y_best_pred = best_dt.predict(X_test)
best_accuracy = accuracy_score(y_test, y_best_pred)

print("Best Decision Tree Parameters:", grid_search.best_params_)
print("Best Decision Tree Accuracy:", round(best_accuracy * 100, 2), "%")

# Visualize tuned tree
plt.figure(figsize=(14, 7))
plot_tree(
    best_dt,
    filled=True,
    feature_names=X.columns,
    class_names=label_encoders["Service Chosen"].classes_,
)
plt.title("Best Tuned Decision Tree")
plt.show()
