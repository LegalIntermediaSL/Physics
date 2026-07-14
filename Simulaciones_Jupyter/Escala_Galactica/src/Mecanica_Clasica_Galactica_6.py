import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 6)
y = np.cos(t + 6)
plt.plot(x, y)
plt.title('Simulation 6')
plt.show()
