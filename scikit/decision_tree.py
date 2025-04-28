import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score

# Create Dataset
print("\nCreating dataset.")
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
print(df)

# Encode Categorical Variables
print("\nEncoding categorical variables.")
label_encoders = {}
df_encoded = df.copy()

for col in ["Referrer", "Location", "Read FAQ", "Service Chosen"]:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df[col])
    label_encoders[col] = le

print("Show head to see how data looks after encoding.")
print(df_encoded.head())

# Train/Test Split
X = df_encoded.drop("Service Chosen", axis=1)
y = df_encoded["Service Chosen"]
# This is where we set the test size and random state
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=49
)
# ------------------------------------------------------------------^^^---------------^^-----

# Train Decision Tree
print("\nTraining Decision Tree classifier.")
tree_clf = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=4)
tree_clf.fit(X_train, y_train)

# Visualize Decision Tree
print("\nPlotting Decision Tree structure.")
plt.figure(figsize=(14, 7))
plot_tree(
    tree_clf,
    feature_names=X.columns,
    class_names=label_encoders["Service Chosen"].classes_,
    filled=True,
    rounded=True,
)
plt.title("Decision Tree Structure")
plt.show()
print("This tree shows how different features are used to split data and decide.")

# Text Tree Representation
print("\nTextual representation of decision tree logic:")
print(export_text(tree_clf, feature_names=list(X.columns)))


# Define Prediction Function
def predict_service(referrer, location, read_faq, pages_viewed):
    input_df = pd.DataFrame(
        [
            {
                "Referrer": label_encoders["Referrer"].transform([referrer])[0],
                "Location": label_encoders["Location"].transform([location])[0],
                "Read FAQ": label_encoders["Read FAQ"].transform([read_faq])[0],
                "Pages viewed": pages_viewed,
            }
        ]
    )

    prediction = tree_clf.predict(input_df)
    predicted_label = label_encoders["Service Chosen"].inverse_transform(prediction)[0]
    print(
        f"Prediction for user (Referrer={referrer}, Location={location}, FAQ={read_faq}, Pages={pages_viewed}): {predicted_label}"
    )
    return predicted_label


# Predictions
print("\nMaking predictions for new users.")
predict_service("(direct)", "USA", "yes", 5)
predict_service("google", "UK", "no", 20)
predict_service("slashdot", "France", "yes", 10)
predict_service("kiwitobes", "UK", "no", 22)
predict_service("digg", "USA", "yes", 25)

# Evaluate Accuracy
print("\nEvaluating model accuracy.")
y_pred = tree_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Decision Tree on test data: {accuracy * 100:.2f}%")
print(
    "Accuracy is percentage of correct predictions made by model on unseen test data."
)

# Feature Importance
print("\nAnalyzing feature importances.")
importances = tree_clf.feature_importances_
plt.figure(figsize=(8, 5))
sns.barplot(x=importances, y=X.columns)
plt.title("Feature Importances from Decision Tree")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.show()
print(
    "This bar chart shows how important each feature was in making splits within tree."
)
print(
    "Higher scores indicate model relied more on that feature when deciding which branch to follow."
)

# Test Set Predictions
print("\nPredicting on test cases and comparing results.")
print(
    "Here is bottom line. We look a the predictions on test data, along with the actual labels."
)

# Inverse transform for human-readable labels
y_test_decoded = label_encoders["Service Chosen"].inverse_transform(y_test)
y_pred_decoded = label_encoders["Service Chosen"].inverse_transform(y_pred)

X_test_reset = X_test.reset_index(drop=True)

for i in range(len(X_test)):
    input_features = X_test_reset.iloc[i]
    predicted = y_pred_decoded[i]
    actual = y_test_decoded[i]
    correct = "✓" if predicted == actual else "✗"

    referrer = label_encoders["Referrer"].inverse_transform(
        [input_features["Referrer"]]
    )[0]
    location = label_encoders["Location"].inverse_transform(
        [input_features["Location"]]
    )[0]
    read_faq = label_encoders["Read FAQ"].inverse_transform(
        [input_features["Read FAQ"]]
    )[0]
    pages = input_features["Pages viewed"]

    print(
        f"Test case {i+1}: Referrer={referrer}, Location={location}, FAQ={read_faq}, Pages={pages} => Predicted: {predicted}, Actual: {actual} [{correct}]"
    )
