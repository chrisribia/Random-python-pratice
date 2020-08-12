import numpy as np
from sklearn import preprocessing
# Create feature
feature = np.array([[-500.5],
                     [-100.1],
                     [0],
                     [100.1],
                     [900.9]])
# Create scaler
scaler = preprocessing.StandardScaler()

# Scale feature
stdized = scaler.fit_transform(feature)
# Show feature
print(stdized)