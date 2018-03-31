from sklearn.cluster import KMeans
import numpy as np

np.random.seed(199999)

means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]

N = 500

X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis = 0)

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

print('Centers found by scikit-learn:')
print(kmeans.cluster_centers_)

pred_label = kmeans.predict(X)
print(pred_label)

# kmeans_display(X, pred_label)