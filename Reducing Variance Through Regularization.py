from sklearn.svm import LinearSVC
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
from matplotlib import pyplot as plt


iris = datasets.load_iris()
features = iris.data[:100,:2]
target = iris.target[:100]

scaler = StandardScaler()
features_std = scaler.fit_transform(features)


svc = LinearSVC(C=15)
model = svc.fit(features_std,target)


color = ["black" if c==0 else "lightgrey" for c in target]

plt.scatter(features_std[:,0],features_std[:,1],c=color)

w = svc.coef_[0]
a = -w[0]/w[1]
xx = np.linspace(-2.5,2.5)
yy = a * xx - (svc.intercept_[0]/w[1])
plt.plot(xx,yy)
plt.axis("off")
plt.show()
