import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 32)
y = np.cos(t + 32)
plt.plot(x, y)
plt.title('Simulation 32')
plt.show()
