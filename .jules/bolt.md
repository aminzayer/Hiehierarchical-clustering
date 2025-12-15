## 2025-05-23 - Scipy Linkage Optimization
**Learning:** `scipy.cluster.hierarchy.linkage` accepts a condensed distance matrix (from `scipy.spatial.distance.pdist`) for all common linkage methods ('single', 'complete', 'average', 'ward', 'centroid', 'median'), avoiding redundant distance calculations when clustering the same dataset with multiple methods.
**Action:** When performing hierarchical clustering on the same dataset with multiple linkage methods, precompute the distance matrix using `pdist` and pass it to `linkage` to improve performance.
