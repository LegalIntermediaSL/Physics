import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 33)
y = np.cos(t + 33)
plt.plot(x, y)
plt.title('Simulation 33')
plt.show()
