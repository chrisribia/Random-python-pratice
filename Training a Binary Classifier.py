from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
features = iris.data[:100,:]
target = iris.target[:100]

scaler = StandardScaler()
features_std = scaler.fit_transform(features)

logist_regression = LogisticRegression(random_state=0)

model = logist_regression.fit(features_std,target)

new_observation =[[0.1,0.1,-0.1,-0.1]]
pred = model.predict(new_observation)

print(model.predict_proba(new_observation))
print(pred)