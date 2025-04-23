import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from sklearn.manifold import TSNE
import pandas as pd
import warnings

# Ignore warnings for cleaner output
warnings.filterwarnings("ignore")

# Load and explore the dataset
print("Loading the digits dataset...")
digits = load_digits()
X = digits.data  # Flattened image data (64 features per sample)
y = digits.target  # True labels (0 through 9)

print(f"\nDataset contains {X.shape[0]} samples with {X.shape[1]} features each.")
print("Displaying sample images of the digits...")

plt.figure(figsize=(16, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X[i, :].reshape(8, 8), cmap="gray")
    plt.title(f"Label: {y[i]}")
    plt.axis("off")
plt.suptitle("Sample Digit Images", fontsize=16)
plt.tight_layout()
plt.show()

# PCA Projection to 2D
print("\nReducing data dimensions to 2D")
pca = decomposition.PCA(n_components=2)
X_reduced = pca.fit_transform(X)

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
plt.title("PCA Projection of Digits Data (2D)", fontsize=14)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.tight_layout()
plt.show()

# t-SNE Projection to 2D
print("\nTry t-SNE for better visualization of clusters")
tsne = TSNE(random_state=17, init="pca", learning_rate="auto")
X_tsne = tsne.fit_transform(X)

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
plt.title("t-SNE Projection of Digits Data (2D)", fontsize=14)
plt.xlabel("t-SNE Feature 1")
plt.ylabel("t-SNE Feature 2")
plt.grid(True)
plt.tight_layout()
plt.show()

# PCA Explained Variance Plot
print("\nCalculating explained variance for all PCA components.")
pca_full = decomposition.PCA().fit(X)

plt.figure(figsize=(10, 7))
plt.plot(np.cumsum(pca_full.explained_variance_ratio_), color="k", lw=2)
plt.axvline(21, color="blue", linestyle="--", label="21 Components")
plt.axhline(0.9, color="red", linestyle="--", label="90% Variance")
plt.xlabel("Number of PCA Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("Explained Variance by PCA Components", fontsize=14)
plt.xticks(np.arange(0, 65, 5))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Elbow Method for KMeans Clustering
print("\nApplying KMeans clustering and using the Elbow Method to find optimal k.")

inertia = []
k_range = range(1, 16)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_reduced)  # using PCA-reduced data for performance
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(k_range, inertia, marker="o", linestyle="--", color="purple")
plt.title("Elbow Method for Optimal Number of Clusters (on PCA Data)", fontsize=14)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Within-Cluster Sum of Squares (Inertia)")
plt.xticks(k_range)
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualizing Clusters
print("\nVisualizing the clusters identified by KMeans.")
kmeans_final = KMeans(n_clusters=10, random_state=42)
clusters = kmeans_final.fit_predict(X_reduced)

# Combine data for plotting
clustered_data = pd.DataFrame(X_reduced, columns=["PC1", "PC2"])
clustered_data["Cluster"] = clusters

plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    clustered_data["PC1"],
    clustered_data["PC2"],
    c=clustered_data["Cluster"],
    cmap="tab10",
    edgecolor="k",
    s=100,
    alpha=0.8,
)
plt.title("KMeans Clusters on PCA-Reduced Digits Data", fontsize=14)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.tight_layout()
plt.show()
