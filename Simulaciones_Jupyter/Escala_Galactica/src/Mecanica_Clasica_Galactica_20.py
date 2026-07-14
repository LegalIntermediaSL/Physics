import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 20)
y = np.cos(t + 20)
plt.plot(x, y)
plt.title('Simulation 20')
plt.show()
