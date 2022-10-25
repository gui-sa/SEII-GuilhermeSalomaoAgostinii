import numpy as np

a = np.random.random((3,2)) #mean 0 an var 1.... 3 rows and 2 cols
print(a)

a = np.random.randn(3,2) #normal/ gaussian distro
print(a)
print(a.mean(), a.var())

a = np.random.randint(3,10,size=(3,3)) #from 3 to 10... 3 rows and 3 cols
print(a)

a = np.random.choice(5, size=10) #between 0 and 5
print(a)

a = np.random.choice([5,-10,3,6,7], size=10) #between the list options
print(a)
