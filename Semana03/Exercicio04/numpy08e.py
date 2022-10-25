import numpy as np

a = np.array([10,19,39,41,50,61])
print(a)

b = [1,3,5]
print(a[b]) #fancy indexing... you index the values of a list or array into an array

even = np.argwhere(a%2==0).flatten() # returns its index of the values that passes the condition
print(a[even]) #will filter just the even values

