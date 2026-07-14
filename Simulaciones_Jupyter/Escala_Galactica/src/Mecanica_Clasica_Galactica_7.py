import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 7)
y = np.cos(t + 7)
plt.plot(x, y)
plt.title('Simulation 7')
plt.show()
