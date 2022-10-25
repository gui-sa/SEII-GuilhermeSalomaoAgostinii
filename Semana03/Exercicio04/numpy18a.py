import numpy as np

data = np.loadtxt('spambase.csv', delimiter=',', dtype=np.float32)
print(data.shape)
