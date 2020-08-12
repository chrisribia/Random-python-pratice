from sklearn.linear_model import LogisticRegression
from sklearn import  datasets
from sklearn.preprocessing import  StandardScaler


iris = datasets.load_iris()
features = iris.data
target = iris.target

scaler = StandardScaler()
features_std = scaler.fit_transform(features)

logistic_regression = LogisticRegression(random_state=0, multi_class='ovr')

model = logistic_regression.fit(features_std,target)