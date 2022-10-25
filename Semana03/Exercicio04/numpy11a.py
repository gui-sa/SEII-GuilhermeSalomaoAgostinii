import numpy as np


# broadcast allows array operations with diferent shapes

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
a = np.array([1,0,1])

#for each element (1,3) inside it, it will broad cast element correspondent to each (1,3) element

y = x + a
print(y)





