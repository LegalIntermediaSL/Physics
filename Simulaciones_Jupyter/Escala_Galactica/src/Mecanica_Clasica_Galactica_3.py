import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 3)
y = np.cos(t + 3)
plt.plot(x, y)
plt.title('Simulation 3')
plt.show()
