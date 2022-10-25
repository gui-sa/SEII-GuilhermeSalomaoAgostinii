import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

#stack horizontally
c = np.hstack((a,b)) #inside of a tuple returns and stacks it horizontally
print(c)

#stack vertically
c = np.vstack((a,b)) #inside of a tuple returns and stacks it vertically
print(c)
