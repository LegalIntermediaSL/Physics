import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 15)
y = np.cos(t + 15)
plt.plot(x, y)
plt.title('Simulation 15')
plt.show()
