from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline,FeatureUnion
from sklearn.model_selection import GridSearchCV

iris = datasets.load_iris()
feature = iris.data
target = iris.target


standadizer = StandardScaler()

feature_std = standadizer.fit_transform(feature)

knn = KNeighborsClassifier(n_neighbors=5,n_jobs=-1)

pipe = Pipeline([("standadizer",standadizer),("knn",knn)])


search_space =[{"knn__n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}]

classifier = GridSearchCV(pipe,search_space,cv=5,verbose=0).fit(feature_std,target)
No_of_classes = classifier.best_estimator_.get_params()["knn__n_neighbors"]
print(No_of_classes)