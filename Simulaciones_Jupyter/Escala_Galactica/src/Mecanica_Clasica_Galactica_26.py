import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 26)
y = np.cos(t + 26)
plt.plot(x, y)
plt.title('Simulation 26')
plt.show()
