import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 12)
y = np.cos(t + 12)
plt.plot(x, y)
plt.title('Simulation 12')
plt.show()
