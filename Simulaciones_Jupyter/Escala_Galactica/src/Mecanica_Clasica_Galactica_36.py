import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 36)
y = np.cos(t + 36)
plt.plot(x, y)
plt.title('Simulation 36')
plt.show()
