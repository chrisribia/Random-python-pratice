# Load libraries

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target

standardizer = StandardScaler()


x_std = standardizer.fit_transform(x)
knn = KNeighborsClassifier(n_neighbors=5,n_jobs=-1).fit(x_std,y)


# Create two observations
new_observations = [ 
 [ 1, 1, 1, 1]]


print(knn.predict(new_observations))