import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 10)
y = np.cos(t + 10)
plt.plot(x, y)
plt.title('Simulation 10')
plt.show()
