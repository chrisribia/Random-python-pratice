import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
# Create feature
# Create feature
feature = np.array([["Texas"],
 ["California"],
 ["Texas"],
 ["Delaware"],
 ["Texas"]])
# Create one-hot encoder
one_hot = LabelBinarizer()
# One-hot encode feature
one_hot.fit_transform(feature)
# Reverse one-hot encoding
one_hot.inverse_transform(one_hot.transform(feature))
print(
one_hot.inverse_transform(one_hot.transform(feature)))
# Import library
import pandas as pd
# Create dummy variables from feature
dt = pd.get_dummies(feature[:,0])
print(dt)