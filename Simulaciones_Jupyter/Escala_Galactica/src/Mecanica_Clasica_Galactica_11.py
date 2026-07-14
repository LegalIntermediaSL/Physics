import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 11)
y = np.cos(t + 11)
plt.plot(x, y)
plt.title('Simulation 11')
plt.show()
