import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 14)
y = np.cos(t + 14)
plt.plot(x, y)
plt.title('Simulation 14')
plt.show()
