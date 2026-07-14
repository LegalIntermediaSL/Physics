import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 16)
y = np.cos(t + 16)
plt.plot(x, y)
plt.title('Simulation 16')
plt.show()
