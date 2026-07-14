import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)
plt.contourf(X, Y, Z)
