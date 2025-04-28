import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# 1. Load the training data
data = np.loadtxt("points_training.txt")
X = data[:, 0]
Y = data[:, 1]
labels = data[:, 2]

# 2. Define styles for each class
class_styles = {
    1: {"marker": "o", "color": "red"},
    2: {"marker": "s", "color": "green"},
    3: {"marker": "^", "color": "blue"},
}

# 3. Plot the training points
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

# 4. Train k-NN classifier
train_XY = np.column_stack((X, Y))
k = 11
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(train_XY, labels)
print(f"k-NN classifier trained with k={k}")

# 5. Create a mesh grid over the feature space
x_min, x_max = X.min() - 5, X.max() + 5
y_min, y_max = Y.min() - 5, Y.max() + 5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))

# 6. Predict labels over the grid
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 7. Plot the decision boundary
plt.figure(figsize=(8, 6))
plt.contourf(
    xx, yy, Z, alpha=0.3, levels=[0.5, 1.5, 2.5, 3.5], colors=["red", "green", "blue"]
)

# 8. Re-plot the training points on top
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
plt.title(f"Training Points with k-NN Decision Boundary (k={k})")
plt.legend()
plt.grid(True)
plt.show()
