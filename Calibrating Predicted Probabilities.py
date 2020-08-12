# Load libraries
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.calibration import CalibratedClassifierCV
# Load data
iris = datasets.load_iris()
features = iris.data
target = iris.target
# Create Gaussian Naive Bayes object
classifer = GaussianNB()
# Create calibrated cross-validation with sigmoid calibration
classifer_sigmoid = CalibratedClassifierCV(classifer, cv=2, method='sigmoid')
# Calibrate probabilities
classifer_sigmoid.fit(features, target)
# Create new observation

new_observation = [[ 2.6, 2.6, 2.6, 0.4]]
# View calibrated probabilities
pred = classifer_sigmoid.predict_proba(new_observation)
print(pred)