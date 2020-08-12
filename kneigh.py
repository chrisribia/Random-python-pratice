# Load libraries
from sklearn import datasets
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
# Load data
iris = datasets.load_iris()
features = iris.data

standadizer = StandardScaler()
features_std = standadizer.fit_transform(features)

nearest_neighbours = NearestNeighbors(n_neighbors=3,metric='euclidean').fit(features_std)

# new_observation = [1,1,1,1]
# distance, indices = nearest_neighbours.kneighbors([new_observation])

nearest_neighbours_with_self = nearest_neighbours.kneighbors_graph(features_std).toarray()
# Remove 1's marking an observation is a nearest neighbor to itself
for i, x in enumerate(nearest_neighbours_with_self):
 x[i] = 0
# View first observation's two

print(nearest_neighbours_with_self[0])

