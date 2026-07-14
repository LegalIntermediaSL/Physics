import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 37)
y = np.cos(t + 37)
plt.plot(x, y)
plt.title('Simulation 37')
plt.show()
