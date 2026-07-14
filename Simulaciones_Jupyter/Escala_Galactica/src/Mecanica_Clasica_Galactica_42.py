import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 42)
y = np.cos(t + 42)
plt.plot(x, y)
plt.title('Simulation 42')
plt.show()
