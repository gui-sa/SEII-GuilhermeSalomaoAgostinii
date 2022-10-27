#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from scipy.interpolate import interp1d

x = np.linspace(0,10,10)
y = x**2 * np.sin(x)
plt.scatter(x,y)

f = interp1d(x,y, kind='linear')
x_dense = np.linspace(0,10,10)
y_dense = f(x_dense)

plt.plot(x_dense,y_dense)

f1 = interp1d(x,y, kind='cubic')
y_dense = f1(x_dense)
plt.plot(x_dense,y_dense)
# %%
