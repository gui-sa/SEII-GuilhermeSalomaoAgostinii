import numpy as np


a = np.array([[1,2], [2,3]])

print(np.linalg.inv(a)) # inverse matrix
print(np.linalg.det(a)) # determinant matrix
print(np.diag(a)) # return diagonal elements

