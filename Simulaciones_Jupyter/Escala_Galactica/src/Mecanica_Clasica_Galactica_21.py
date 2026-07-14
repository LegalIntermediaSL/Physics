import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 21)
y = np.cos(t + 21)
plt.plot(x, y)
plt.title('Simulation 21')
plt.show()
