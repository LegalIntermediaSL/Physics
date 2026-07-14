import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 24)
y = np.cos(t + 24)
plt.plot(x, y)
plt.title('Simulation 24')
plt.show()
