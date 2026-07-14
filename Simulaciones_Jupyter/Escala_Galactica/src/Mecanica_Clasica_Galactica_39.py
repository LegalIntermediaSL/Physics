import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 39)
y = np.cos(t + 39)
plt.plot(x, y)
plt.title('Simulation 39')
plt.show()
