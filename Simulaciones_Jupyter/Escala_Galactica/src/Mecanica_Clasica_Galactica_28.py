import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 28)
y = np.cos(t + 28)
plt.plot(x, y)
plt.title('Simulation 28')
plt.show()
