import numpy as np

a = np.array([[1,2],[12,13],[5,7]])
print(a)

bool_idx = a > 2
print(bool_idx) #returns boolean for each element
print(a[bool_idx]) #returns just the true elements! - in a vector , nor matrix
print(a[a>2]) #same thing

b = np.where(a>2, a ,-1) # (condition, values, what to put in the falses)
print(b)
