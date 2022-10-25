import numpy as np

a = np.array([[1,2],[3,4] ])
print(a)

b = np.array([[5,6]]) #it needs to have same shape
c= np.concatenate((a,b)) #inside a tuple
print(c)


c= np.concatenate((a,b), axis=0) #Will maintain
print(c)


c= np.concatenate((a,b), axis=None) #will create a flatten array, but, concatenated
print(c)

c= np.concatenate((a,b.T), axis=1) #will concatenate in the column
print(c)

