import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn import decomposition
from sklearn.manifold import TSNE
import warnings

# Suppress warnings for clean output
warnings.filterwarnings("ignore")

# Load the digits dataset
digits = load_digits()
X = digits.data  # Each image is an 8x8 grid flattened into a 64-feature vector
y = digits.target  # Labels for each image (digits 0 through 9)

# Display 10 sample digit images with their labels
plt.figure(figsize=(16, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X[i, :].reshape(8, 8), cmap="gray")  # Reshape back to 8x8 image
    plt.title(f"Label: {y[i]}")  # Show the true digit label
    plt.axis("off")  # Hide axes for cleaner display
plt.suptitle("Sample Digit Images", fontsize=16)
plt.tight_layout()
plt.show()

# Apply Principal Component Analysis (PCA) to reduce features to 2 dimensions
pca = decomposition.PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(f"Projecting {X.shape[1]}-dimensional data to 2D using PCA")

# Plot the PCA-reduced data
plt.figure(figsize=(12, 10))
scatter = plt.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    c=y,
    cmap="nipy_spectral",
    edgecolor="none",
    alpha=0.7,
    s=40,
)
plt.colorbar(scatter, label="Digit Label")
plt.title("Digits Dataset: PCA Projection to 2D", fontsize=14)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.tight_layout()
plt.show()

# Apply t-SNE for another type of 2D projection (more nonlinear than PCA)
print("Running t-SNE projection (this may take a few seconds)...")
tsne = TSNE(random_state=17, init="pca", learning_rate="auto")
X_tsne = tsne.fit_transform(X)

# Plot the t-SNE-reduced data
plt.figure(figsize=(12, 10))
scatter = plt.scatter(
    X_tsne[:, 0],
    X_tsne[:, 1],
    c=y,
    cmap="nipy_spectral",
    edgecolor="none",
    alpha=0.7,
    s=40,
)
plt.colorbar(scatter, label="Digit Label")
plt.title("Digits Dataset: t-SNE Projection to 2D", fontsize=14)
plt.xlabel("t-SNE Feature 1")
plt.ylabel("t-SNE Feature 2")
plt.grid(True)
plt.tight_layout()
plt.show()

# Apply full PCA to determine how many components explain most of the variance
pca_full = decomposition.PCA().fit(X)

# Plot cumulative explained variance for each number of components
plt.figure(figsize=(10, 7))
plt.plot(np.cumsum(pca_full.explained_variance_ratio_), color="k", lw=2)
plt.axvline(21, color="blue", linestyle="--", label="21 Components")  # Visual guide
plt.axhline(0.9, color="red", linestyle="--", label="90% Variance")  # Target threshold
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("PCA Explained Variance by Components", fontsize=14)
plt.xticks(np.arange(0, 65, 5))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Use the Elbow Method to help choose an appropriate number of clusters (k)
inertia = []  # List to store WCSS for each value of k
k_range = range(1, 11)  # Test k values from 1 to 10

# Run KMeans clustering for each k and store the inertia
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_reduced)  # Use 2D PCA-reduced data
    inertia.append(kmeans.inertia_)

# Plot the Elbow Curve to visualize where the inertia starts leveling off
plt.figure(figsize=(8, 6))
plt.plot(k_range, inertia, marker="o", linestyle="--", color="purple")
plt.title("Elbow Method for Optimal k (on PCA-reduced Digits Data)", fontsize=14)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia (Within-Cluster Sum of Squares)")
plt.xticks(k_range)
plt.grid(True)
plt.tight_layout()
plt.show()
