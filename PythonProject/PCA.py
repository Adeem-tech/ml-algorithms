import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [4, 11],
    [8, 4],
    [13, 6],
    [7, 14]
], dtype=float)

print("Original Data:\n", X)

mean = np.mean(X, axis=0)
X_centered = X - mean

print("\nMean of each feature:", mean)
print("\nCentered Data:\n", X_centered)

cov_matrix = np.cov(X_centered.T)

print("\nCovariance Matrix:\n", cov_matrix)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)

idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("\nSorted Eigenvalues:\n", eigenvalues)
print("\nSorted Eigenvectors:\n", eigenvectors)

principal_component = eigenvectors[:, 0].reshape(-1, 1)

print("\nPrincipal Component:\n", principal_component)

X_pca = X_centered.dot(principal_component)

print("\nData after PCA (1D):\n", X_pca)

plt.figure()
plt.scatter(X[:,0], X[:,1])
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Original Data")
plt.show()

plt.figure()
plt.scatter(X_pca, np.zeros_like(X_pca))
plt.xlabel("Principal Component 1")
plt.title("Data after PCA (1 Dimension)")
plt.yticks([])
plt.show()
