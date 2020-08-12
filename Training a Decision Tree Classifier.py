from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets


iris = datasets.load_iris()
feature = iris.data
target = iris.target

decisiontree = DecisionTreeClassifier(random_state=0)

model = decisiontree.fit(feature,target)