from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import numpy as np

# ⚡ Bolt Optimization: Precompute distance matrix to avoid recalculating it for each linkage method
# This reduces the computational complexity when trying multiple clustering methods on the same data.

X = np.array([[1, 3], [4, 2], [5, 6], [3, 1], [7, 2], [3, 3]], dtype=float)

# Precompute the distance matrix
distance_matrix = pdist(X, metric='euclidean')

# Define labels once
labelList = range(1, 7)

#Plotting Data
plt.figure(figsize=(7, 3))
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:, 0], X[:, 1], label='True Position')

for label, x, y in zip(labelList, X[:, 0], X[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')
plt.show()

## Use Hierarchical Algorithm Single Method
# Pass precomputed distance matrix
linked = linkage(distance_matrix, 'single')
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top',labels=labelList,distance_sort='descending',show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Complete Method
linked = linkage(distance_matrix, 'complete')
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Average Method
linked = linkage(distance_matrix, 'average')
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Ward Method
linked = linkage(distance_matrix, 'ward')
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Centroid Method
linked = linkage(distance_matrix, 'centroid')
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()

# Use Hierarchical Algorithm Median Method
linked = linkage(distance_matrix, 'median')
plt.figure(figsize=(7, 3))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.show()
