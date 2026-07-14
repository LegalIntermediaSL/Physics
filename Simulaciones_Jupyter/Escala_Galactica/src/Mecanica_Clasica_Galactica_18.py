import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 18)
y = np.cos(t + 18)
plt.plot(x, y)
plt.title('Simulation 18')
plt.show()
