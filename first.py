# Data preprocessing
import numpy as np
from sklearn import preprocessing

input_data = np.array([[2.2, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [5.9, 2.3, -5.8]])

data_binarized = preprocessing.Binarizer(threshold=0.0).transform(input_data)
print(data_binarized)