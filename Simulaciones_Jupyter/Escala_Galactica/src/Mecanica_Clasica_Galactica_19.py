import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 19)
y = np.cos(t + 19)
plt.plot(x, y)
plt.title('Simulation 19')
plt.show()
