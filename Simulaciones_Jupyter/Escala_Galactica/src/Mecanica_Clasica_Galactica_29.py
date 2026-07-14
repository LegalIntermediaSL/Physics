import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 29)
y = np.cos(t + 29)
plt.plot(x, y)
plt.title('Simulation 29')
plt.show()
