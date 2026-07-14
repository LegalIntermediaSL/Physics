import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 40)
y = np.cos(t + 40)
plt.plot(x, y)
plt.title('Simulation 40')
plt.show()
