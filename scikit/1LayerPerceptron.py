import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# References:
# make_classification documentation: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html

# Make Classification - Generates a random n-class classification problem
# Change the seed to get different data
X, y = make_classification(
    n_samples=100,  # Number of samples
    n_features=2,  # Number of features
    n_informative=2,  # Number of informative features
    n_redundant=0,  # Number of redundant features
    n_classes=2,  # Number of classes, or labels
    n_clusters_per_class=1,  # Number of clusters per class
    class_sep=2.0,  # Class separation, factor by which classes are separated
    random_state=84,  # Seed for reproducibility
)

# y was type float64, convert to int - this helps processing
y = y.astype(int)


class Perceptron:
    def __init__(self, lr=0.01, n_epochs=150):
        self.lr = lr
        self.n_epochs = n_epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.n_epochs):
            for index, x in enumerate(X):
                # Compute linear output, dot product of input features and weights - add bias
                linear_output = np.dot(x, self.weights) + self.bias

                # _activation step with linear output
                y_pred = self._activation(linear_output)

                # Update weights and bias using learning rate and error
                update = self.lr * (y[index] - y_pred)

                # Update weights with scaled update and input features
                self.weights += update * x

                # Update bias by adding scaled update value
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return self._activation(linear_output)

    def _activation(self, x):
        return np.where(x >= 0, 1, 0)


# 1. Train Perceptron
model = Perceptron(lr=0.01, n_epochs=100)
model.fit(X, y)
predictions = model.predict(X)

# 2. Evaluate and make a nice graph
acc = accuracy_score(y, predictions)  # Tool to evaluate accuracy with predictions
print(f"Training Accuracy: {acc * 100:.2f}%")  # Show the accuracy


# Decision Boundary Plot Method
# References: https://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
def plot_decision_boundary(X, y, model):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))
    grid = np.c_[xx.ravel(), yy.ravel()]
    preds = model.predict(grid).reshape(xx.shape)

    # Create plot
    plt.figure(figsize=(10, 6))

    # Plot decision boundary
    plt.contourf(xx, yy, preds, alpha=0.3, cmap=plt.cm.coolwarm)

    # Scatter plot of data points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors="k", s=50)

    # Add labels, title, and grid
    plt.title("Perceptron Decision Boundary", fontsize=16, fontweight="bold")
    plt.xlabel("Feature 1", fontsize=12)
    plt.ylabel("Feature 2", fontsize=12)
    plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)

    plt.show()


plot_decision_boundary(X, y, model)
