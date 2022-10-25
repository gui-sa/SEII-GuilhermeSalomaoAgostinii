import numpy as np

a = np.array([1,2,3])
b  = a
b[0] = 42

print(b)
print(a)
print(a is b) #they point to the same place in the memory

b = np.copy(a)
b[0] = 420
print(b)
print(a)
print(a is b)

