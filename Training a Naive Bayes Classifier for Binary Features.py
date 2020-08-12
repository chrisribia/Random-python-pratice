import numpy as np
from sklearn.naive_bayes import BernoulliNB

feature = np.random.randint(2,size=(100, 3))
target = np.random.randint(2,size=(100,1)).ravel()


classifier = BernoulliNB(class_prior=[0.25,0.5])

model = classifier.fit(feature,target)