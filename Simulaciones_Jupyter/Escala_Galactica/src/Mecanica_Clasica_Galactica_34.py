import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 34)
y = np.cos(t + 34)
plt.plot(x, y)
plt.title('Simulation 34')
plt.show()
