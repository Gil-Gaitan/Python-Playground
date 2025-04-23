import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import preprocessing

# Credit: https://www.kaggle.com/code/jasleensondhi/k-means-clustering-on-iris-data-elbow-method

# Load the iris dataset from seaborn
iris_df = sns.load_dataset("iris")

print("Iris dataset loaded successfully")
print("\nValues in the 'species' column. There are 3 species in the dataset:")
print(iris_df["species"].value_counts())

print("\nPreview of the dataset:")
print(iris_df.head())

# Visualize the distribution of sepal length vs sepal width with species hue
print("\nPlotting sepal_length vs sepal_width colored by species")
plt.figure(figsize=(10, 7))
sns.scatterplot(
    x="sepal_length", y="sepal_width", hue="species", data=iris_df, palette="inferno"
)
plt.title("Sepal Length vs Sepal Width by Species", fontsize=14)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend(title="Species")
plt.grid(True)
plt.tight_layout()
plt.show()

# Encode species labels into numerical format
label_encoder = preprocessing.LabelEncoder()
iris_df["species"] = label_encoder.fit_transform(iris_df["species"])

print("Splitting the dataset into features (X) and target (y)")
X = iris_df[["sepal_length", "petal_width"]]  # Features used for clustering
y = iris_df["species"]

# Apply KMeans with 3 clusters (we know there are 3 species)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Predict cluster labels
identified_clusters = kmeans.predict(X)

# Use the elbow method to find the optimal number of clusters
distance = []  # Store Within-Cluster Sum of Squares (WCSS) for each k
for i in range(1, 7):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X)
    distance.append(kmeans.inertia_)  # WCSS for current k

# Plot the Elbow Method result
print("\nPlotting the Elbow Method to choose optimal k")
plt.figure(figsize=(8, 6))
plt.plot(range(1, 7), distance, marker="o", linestyle="--", color="b")
plt.title("Elbow Method for Optimal Number of Clusters", fontsize=14)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Within-Cluster Sum of Squares (WCSS)")
plt.grid(True)
plt.xticks(range(1, 7))
plt.tight_layout()
plt.show()

# Add cluster labels to the dataset
data_with_clusters = X.copy()
data_with_clusters["Cluster"] = identified_clusters

# Plot final clusters based on sepal length and petal width
print("Visualizing clusters found by KMeans")
fig, ax = plt.subplots(figsize=(10, 8))

scatter = ax.scatter(
    data_with_clusters["sepal_length"],
    data_with_clusters["petal_width"],
    c=data_with_clusters["Cluster"],
    cmap="winter",
    edgecolor="k",
    s=100,
    alpha=0.8,
)

ax.set_title("KMeans Clustering: Sepal Length vs Petal Width", fontsize=14)
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Petal Width (cm)")
ax.legend(*scatter.legend_elements(), title="Cluster")
ax.grid(True)
plt.tight_layout()
plt.show()
