import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 46)
y = np.cos(t + 46)
plt.plot(x, y)
plt.title('Simulation 46')
plt.show()
