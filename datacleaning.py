from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
iris_datasets = load_iris()
X_train,X_test,y_train,y_test = \
    train_test_split(iris_datasets['data'],iris_datasets['target'],random_state=0)

knn.fit(X_train,y_train)

X_new = np.array([[0.5,0.9,1,0.2]])

y_pred = knn.predict(X_test)
print(knn.score(X_test,y_test))