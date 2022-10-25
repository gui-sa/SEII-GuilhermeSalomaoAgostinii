import numpy as np


a = np.array([1,2])
print(a.shape)

a = np.array([[1,2], [2,3],[3,4]])
print(a.shape)

#( ROWS, COLUMNS )

print(a[0][0]) #first row at  that vector extracted, get the first element again
print(a[0,0]) #first row, first column - slicing
print(a[:,0]) #all rows, first column - slicing
print(a[0,:]) #first row, all columns 
print(a.T) #transposed
print(a.linalg.inv()) # inverse matrix

