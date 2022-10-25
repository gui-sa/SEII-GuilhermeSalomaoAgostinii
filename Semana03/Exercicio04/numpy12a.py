import numpy as np


a = np.array([[7,8,9,10,11,12,13],[17,18,19,12,20,21,22]])

print(a)
print(a.sum(axis = None))
print(a.sum(axis = 0))
print(a.sum(axis = 1))
print(a.mean(axis = None))
print(a.mean(axis = 0))
print(a.mean(axis = 1))
print(a.std(axis = None))
print(a.std(axis = 0))
print(a.std(axis = 1))
print(a.max(axis = None))
print(a.max(axis = 0))
print(a.max(axis = 1))
print(a.min(axis = None))
print(a.min(axis = 0))
print(a.min(axis = 1))
