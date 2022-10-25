import numpy as np


a = np.zeros((2,3)) #2 rows and 3 cols of zeros
print(a)

a = np.ones((2,3)) #2 rows and 3 cols of ones
print(a)
print(a.dtype)

a = np.full((2,3),5.0) #2 rows and 3 cols of .. in this case with 5.0
print(a)
print(a.dtype)

a = np.eye(3) #identity matrix
print(a)
print(a.dtype)

a = np.arange(2,5) #2 to 5 (5 not included)
print(a)

a = np.linspace(0,10,5) #from 0 until 10 (10 included) divided into 5 spaces
print(a)

