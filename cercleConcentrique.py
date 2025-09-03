# cercle concentrique

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
xs, ys = np.meshgrid(x, y, sparse=True)
zs = np.sqrt(xs**2 + ys**2)
h = plt.contourf(x, y, zs)
plt.axis('scaled')
plt.colorbar()
plt.show()
