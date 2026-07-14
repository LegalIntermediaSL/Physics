import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 48)
y = np.cos(t + 48)
plt.plot(x, y)
plt.title('Simulation 48')
plt.show()
