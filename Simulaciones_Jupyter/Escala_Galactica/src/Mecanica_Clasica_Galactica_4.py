import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 4)
y = np.cos(t + 4)
plt.plot(x, y)
plt.title('Simulation 4')
plt.show()
