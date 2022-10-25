import numpy as np

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvector = np.linalg.eig(a)
print(eigenvalues, '\n\n',eigenvector)


b = eigenvector[:,0]*eigenvalues[0]
print(b)

c = a @ eigenvector[:,0] 
print(b)

#print(b==c) #not a good way to compare values because of the floaar caracteristic

print(np.allclose(b,c))



