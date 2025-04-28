import numpy as np
import matplotlib.pyplot as plt

# Load training training and test data
training_data = np.loadtxt("points_training.txt")
test_data = np.loadtxt("points_test.txt")
print("Data loaded from points_training.txt and points_test.txt")
# Print first few rows of training data
print("Training data:")
print(training_data[:5])
print("Test data:")
print(test_data[:5])

print("Step 1: Visualize training points")
# Split training_data into X, Y coordinates and labels to visualize
X = training_data[:, 0]
Y = training_data[:, 1]
labels = training_data[:, 2]

# Define marker style for visualization
class_styles = {
    1: {"marker": "o", "color": "red"},
    2: {"marker": "s", "color": "green"},
    3: {"marker": "^", "color": "blue"},
}

# Display visualization of training points
plt.figure(figsize=(8, 6))
for class_value, style in class_styles.items():
    idx = labels == class_value
    plt.scatter(
        X[idx],
        Y[idx],
        marker=style["marker"],
        color=style["color"],
        label=f"Class {int(class_value)}",
        edgecolors="k",
        s=100,
    )
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.title("Training Points Visualization")
plt.legend()
plt.grid(True)
plt.show()

# KNN Algorithm Implementation
# 1. Takes a new point (x, y) from test
# 2. Calculates distance from new point to all training points
# 3. Sorts distances and selects k nearest neighbors
# 4. Assigns class based on k neighbors
# Reference: https://www.geeksforgeeks.org/k-nearest-neighbours/


# Reference: https://www.geeksforgeeks.org/k-nearest-neighbours/
# To calculate distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# Reference: https://www.geeksforgeeks.org/k-nearest-neighbours/ for basic KNN
# Added print statements to show process
# Predict function accepts a point, training data, and selected k)
def knn_predict(test_point, training_data, k):
    distances = []
    for train_point in training_data:
        # Only use x and y for distance calculation
        distance = euclidean_distance(test_point[:2], train_point[:2])
        distances.append((distance, train_point[2]))  # Save (distance, label value)

    # Sort by distance and get k nearest neighbors
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]

    # Print neighbors for this test point
    print(f"\nTest point: {test_point[:2]}")
    print(f"Neighbors (distance, label):")
    for dist, label in neighbors:
        print(f"  Distance: {dist:.2f}, Label: {int(label)}")

    # Voting
    class_votes = {}
    for _, label in neighbors:
        class_votes[label] = class_votes.get(label, 0) + 1

    # Print results
    print("Vote counts:")
    for label, count in class_votes.items():
        print(f"  Label {int(label)}: {count} votes")

    # Decide based on classification
    predicted_class = max(class_votes, key=class_votes.get)
    print(f"Predicted class: {int(predicted_class)}")

    return predicted_class


# CHOOSE K VALUE HERE
#
#
k = 2
#
#

print("\nStep 2: Predict classes for test points")
predictions = []
for test_point in test_data:
    predicted_class = knn_predict(test_point, training_data, k)
    predictions.append(predicted_class)

# Step 3: Visualize predictions and highlight only incorrect ones
print("\nStep 3: Visualizing test points (only incorrect ones marked)")

plt.figure(figsize=(8, 6))

# Plot training points first
for class_value, style in class_styles.items():
    idx = labels == class_value
    plt.scatter(
        X[idx],
        Y[idx],
        marker=style["marker"],
        color=style["color"],
        edgecolors="k",
        s=100,
    )

# Define lighter colors for test points
lighter_colors = {
    1: "#ff9999",  # light red
    2: "#99ff99",  # light green
    3: "#9999ff",  # light blue
}

# Plot test points
for i, test_point in enumerate(test_data):
    predicted_label = predictions[i]
    true_label = test_point[2]

    # Plot test point normally
    plt.scatter(
        test_point[0],
        test_point[1],
        marker=class_styles[predicted_label]["marker"],  # same marker
        color=lighter_colors[predicted_label],  # lighter color
        edgecolors="black",
        linewidths=2,
        s=200,
    )

    # Only if incorrect, draw a red 'X' over it
    if int(predicted_label) != int(true_label):
        plt.scatter(
            test_point[0],
            test_point[1],
            marker="x",
            color="red",  # Red X
            s=150,
            linewidths=3,
        )

plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.title("Training and Test Points (Red X = Incorrect Prediction)")
plt.grid(True)
plt.show()

# Step 4: Calculate and print accuracy
correct_predictions = 0
total_predictions = len(test_data)

# Compare predictions with true labels
for i, test_point in enumerate(test_data):
    predicted_label = predictions[i]
    true_label = test_point[2]

    if int(predicted_label) == int(true_label):
        correct_predictions += 1

accuracy = (correct_predictions / total_predictions) * 100

# Print accuracy
print(
    f"Bottom Line: With a k of {k}, Accuracy is {accuracy:.2f}%. {correct_predictions} correct out of {total_predictions} test points."
)

# Get accuracy for different values of k
k_values = range(1, 11)  # k from 1 to 10
accuracies = []  # List to store accuracies

# Run KNN for each k value
for k in k_values:
    predictions = []  # Reset predictions for each k
    for test_point in test_data:
        predicted_class = knn_predict(
            test_point, training_data, k
        )  # Get prediction for current k
        predictions.append(predicted_class)

    # Calculate accuracy for current k
    correct_predictions = sum(
        1
        for i, test_point in enumerate(test_data)
        if int(predictions[i]) == int(test_point[2])
    )
    accuracy = (correct_predictions / len(test_data)) * 100
    accuracies.append(accuracy)

# Plot graph
plt.figure(figsize=(8, 6))
plt.plot(k_values, accuracies, marker="o", color="blue", linestyle="-", markersize=8)
plt.xlabel("k (Number of Neighbors)")
plt.ylabel("Accuracy (%)")
plt.title("Accuracy vs. k (Number of Neighbors) for KNN")
plt.grid(True)
plt.show()
