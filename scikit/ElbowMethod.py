import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris, load_digits
from sklearn.preprocessing import StandardScaler


# ---------- Helper function to run Elbow Method and plot ----------
def elbow_method(data, dataset_name, max_k=10):
    print(f"\n[INFO] Running Elbow Method on {dataset_name} dataset...")

    sse = []  # Sum of Squared Errors

    # Try K from 1 to max_k
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
        kmeans.fit(data)
        sse.append(kmeans.inertia_)  # inertia_ is the SSE

    # Plot the elbow
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_k + 1), sse, marker="o", linestyle="--", color="teal")
    plt.title(f"Elbow Method for {dataset_name}", fontsize=14)
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Sum of Squared Errors (SSE)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(range(1, max_k + 1))
    plt.tight_layout()
    plt.show()


# ---------- IRIS Dataset ----------
print("[SECTION] Iris Dataset Analysis")
iris = load_iris()
iris_data = StandardScaler().fit_transform(iris.data)  # Normalize features
elbow_method(iris_data, "Iris", max_k=10)
print(
    "[RESULT] The Iris dataset has 3 actual classes. Check if the elbow occurs at k=3."
)

# ---------- MNIST Digits Dataset ----------
print("\n[SECTION] MNIST Digits Dataset Analysis")
digits = load_digits()
digits_data = StandardScaler().fit_transform(digits.data)  # Normalize features
elbow_method(digits_data, "MNIST Digits", max_k=15)
print(
    "[RESULT] The Digits dataset has 10 actual classes (0-9). Look for an elbow near k=10."
)

print("\n[COMPLETE] Elbow Method analysis complete.")
