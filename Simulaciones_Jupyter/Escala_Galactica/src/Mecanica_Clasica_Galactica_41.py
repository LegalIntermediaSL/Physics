import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 41)
y = np.cos(t + 41)
plt.plot(x, y)
plt.title('Simulation 41')
plt.show()
