# PCA Dimensionality Reduction

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset
data = load_iris()
X = data.data

# Standardize data
X_scaled = StandardScaler().fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Reduced Data:")
print(X_pca[:5])

print("Explained Variance:")
print(pca.explained_variance_ratio_)