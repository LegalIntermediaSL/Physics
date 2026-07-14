import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 17)
y = np.cos(t + 17)
plt.plot(x, y)
plt.title('Simulation 17')
plt.show()
