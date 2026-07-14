import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 38)
y = np.cos(t + 38)
plt.plot(x, y)
plt.title('Simulation 38')
plt.show()
