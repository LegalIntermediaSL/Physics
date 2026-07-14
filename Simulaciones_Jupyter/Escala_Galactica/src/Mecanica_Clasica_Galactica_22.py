import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 22)
y = np.cos(t + 22)
plt.plot(x, y)
plt.title('Simulation 22')
plt.show()
