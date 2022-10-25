import numpy as np
from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a) #converting back to a list.
B = list(b)

T = 1000

def dot1(l1,l2):
    dot = 0
    for i in range(len(l1)):
        dot += l1[i]*l2[i]
    return dot

def dot2(a,b):
    return np.dot(a,b)

start = timer()
for t in range(T):
    dot1(A,B)
end = timer()

t1 = end - start

start = timer()
for t in range(T):
    dot2(a,b)
end = timer()

t2 = end - start

print('list calculation', t1)
print('np.dot', t2)
print('ratio', t1/t2)


#Working with numpy arrays is faster... LOT FASTER