import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 8)
y = np.cos(t + 8)
plt.plot(x, y)
plt.title('Simulation 8')
plt.show()
