import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.datasets import load_digits
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# Load dataset
print("Loading dataset...")
print(
    "Using assignment instructions, can display the first sample X[0] as an 8x8 matrix."
)
digits = load_digits()
X, y = digits.data, digits.target

# Display some information as assignment lays out.

print(np.reshape(X[0], (8, 8)))
print("This shows the data structure as an abstraction of the image.")
print(
    "The value must be the location and intensity of the pixel (0-15), and the image is 8x8 pixels (0-7)."
)
print(X.shape)
print(X[0])
plt.gray()  # Use grayscale colormap
# plt.matshow(digits.images[0])  # Plot image index
# plt.show()

print(
    "1797 samples, each has 64 values (8x8 pixels). 10 classes of taget variables (0-9)."
)
# Set random seed for reproducibility
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print("Data successfully split into training (70%) and testing (30%).\n")
# Train MLP classifier
clf = MLPClassifier(hidden_layer_sizes=(256, 128, 64), max_iter=5000, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Model training complete.\n")

# Calculate accuracy
train_acc = accuracy_score(y_train, clf.predict(X_train))
test_acc = accuracy_score(y_test, y_pred)
print("***Assignment Requirement***")
print(f"Train Accuracy: {train_acc * 100:.2f}%")
print(f"Test Accuracy: {test_acc * 100:.2f}%")
print("Train accuracy is 100 because the model knows the training data well now.")
print("Test accuracy is 98.52 when tested on the reserved data.")

# Show correctly classified samples 0-9
print("\nThe model properly classified these images 0-9. Plot the first 10 images.")
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[y_pred == i][0].reshape(8, 8), cmap=plt.cm.gray)
    plt.title(f"Pred: {i}")
    plt.axis("off")
plt.suptitle("Examples of Classified Images")
plt.show()

# Show confusion matrix
print("Confusion matrix shows the misclassifications.")

conf_matrix = confusion_matrix(y_test, y_pred)
df_cm = pd.DataFrame(
    conf_matrix, index=digits.target_names, columns=digits.target_names
)
plt.figure(figsize=(10, 7))
sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.ylabel("True label")
plt.xlabel("Predicted label")
plt.show()

# Find misclassified samples
misclassified_indices = np.where(y_pred != y_test)[0]
misclassified_labels = y_test[misclassified_indices]
misclassified_counts = Counter(misclassified_labels)

# Sort misclassified labels by frequency
most_misclassified = misclassified_counts.most_common(
    6
)  # Top 6 most misclassified digits

# Plot most misclassified images
plt.figure(figsize=(8, 6))
for i, (label, _) in enumerate(most_misclassified):
    index = misclassified_indices[
        np.where(misclassified_labels == label)[0][0]
    ]  # Get one example
    plt.subplot(2, 3, i + 1)
    plt.imshow(X_test[index].reshape(8, 8), cmap=plt.cm.gray)
    plt.title(f"True: {y_test[index]}, Pred: {y_pred[index]}")
    plt.axis("off")

plt.suptitle("Most Frequently Misclassified Digits")
plt.show()
print("We can see these miscalulations are reflected in the confusion matrix above.")
print("This helps us understand how to read a confusion matrix.")
