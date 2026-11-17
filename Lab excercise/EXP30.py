# K-Means Clustering

from sklearn.cluster import KMeans

# Dataset
X = [[1, 2], [2, 3], [3, 4],
     [8, 9], [9, 10], [10, 11]]

# Create K-Means model
model = KMeans(n_clusters=2, random_state=0, n_init=10)

# Train the model
model.fit(X)

# Display clusters
print("Cluster Labels:", model.labels_)
print("Centroids:", model.cluster_centers_)