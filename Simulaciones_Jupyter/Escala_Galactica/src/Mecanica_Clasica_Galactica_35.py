import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 35)
y = np.cos(t + 35)
plt.plot(x, y)
plt.title('Simulation 35')
plt.show()
