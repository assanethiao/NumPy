# cercle concentrique

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
# full coordinate arrays
xx, yy = np.meshgrid(x, y)
zz = np.sqrt(xx**2 + yy**2)
xx.shape, yy.shape, zz.shape
# sparse coordinate arrays
xs, ys = np.meshgrid(x, y, sparse=True)
zs = np.sqrt(xs**2 + ys**2)
xs.shape, ys.shape, zs.shape
np.array_equal(zz, zs)
h = plt.contourf(x, y, zs)
plt.axis('scaled')
plt.colorbar()
plt.show()
