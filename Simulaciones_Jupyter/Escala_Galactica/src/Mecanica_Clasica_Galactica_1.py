import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 1)
y = np.cos(t + 1)
plt.plot(x, y)
plt.title('Simulation 1')
plt.show()
