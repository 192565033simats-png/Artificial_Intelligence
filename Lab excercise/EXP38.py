# K-Means Clustering

from sklearn.cluster import KMeans

X = [
    [1, 2], [2, 3], [3, 4],
    [8, 9], [9, 10], [10, 11]
]

model = KMeans(n_clusters=2, random_state=0, n_init=10)

model.fit(X)

print("Cluster Labels:", model.labels_)
print("Centroids:", model.cluster_centers_)