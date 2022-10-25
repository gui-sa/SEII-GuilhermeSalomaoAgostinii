import numpy as np


#solving linalg problems
A = np.array([[1,1],[1.5,4.0]])
b = np.array([2200,5050])
x = np.linalg.inv(A).dot(b)
print(x)

x = np.linalg.solve(A,b)
print(x)


