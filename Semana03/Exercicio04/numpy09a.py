import numpy as np

a= np.arange(1,7) #creates a array that starts from 1 and go until 7 (not included)
print(a)
print(a.shape)

b = a.reshape((2,3))#pass a tuple with the desired shape ... rows, cols
print(b)
print(b.shape)
#if a shape isnt possible, it will present an error.

b = a[np.newaxis, :] #will extends a dimension in that position
print(b)
print(b.shape)

b = a[:,np.newaxis] 
print(b)
print(b.shape)