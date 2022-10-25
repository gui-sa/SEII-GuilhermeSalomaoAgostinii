import numpy as np

a = np.array([1,2,3]) #creates an array
print(a) 
print(a.shape) #shape of this array
print(a.dtype) #data type used
print(a.ndim) #number of dimensions
print(a.size) #total number of elements
print(a.itemsize) #size in bytes of this element
print(a[0]) 
a[0] = 10
print(a[0]) #assigning the first element
b = a * np.array([2,0,3]) #each value will multiply with the proper position
print(b)

