from sklearn import datasets
from sklearn.naive_bayes import  GaussianNB

iris = datasets.load_iris()
feature = iris.data
target = iris.target

classifier = GaussianNB(priors=[0.25, 0.25, 0.5])

model = classifier.fit(feature,target)

new_observation = [[4,4,4,0.4]]
pred = model.predict(new_observation)
print(pred)

