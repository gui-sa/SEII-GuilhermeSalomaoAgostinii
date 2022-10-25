import numpy as np

a = np.array([[1,2,10,11,12,13], [2,3,4,5,6,7]])
print(a)

b = a[0,1] #row 0 col 1
print (b)

b = a[0,1:4] #row 0 from col 1 to col 4 col4 not included.
print (b)

b = a[:,0] #all rows, col 0
print (b)

b = a[-1,-2] #last row, two elements from last to beginning.
print (b)