from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.linear_model import RidgeCV
boaton = load_boston()
feature = boaton.data
target = boaton.target

scaler = StandardScaler()
feature_standardized = scaler.fit_transform(feature)


regression = LinearRegression()
model = regression.fit(feature_standardized,target)

regressionR = Ridge(alpha=0.5)
modelR = regressionR.fit(feature_standardized,target)

regressionL = Lasso(alpha=0.5)
modelL = regressionL.fit(feature_standardized,target)

print("Linear regression",model.coef_)
print("Linear regressionR",modelR.coef_)
print("Linear regressionL",modelL.coef_)