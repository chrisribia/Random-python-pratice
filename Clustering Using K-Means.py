# Load libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# Load data
iris = datasets.load_iris()
features = iris.data

# Standardize features
scaler = StandardScaler()
features_std = scaler.fit_transform(features)

# Create k-mean object
cluster = KMeans(n_clusters=3, random_state=0)
# Train model
model = cluster.fit(features_std)

new_observation = [[0.8, 0.8, 0.8, 0.8]]
# Predict observation's cluster
pred = model.predict(new_observation)
print(pred)
print(model.cluster_centers_)


