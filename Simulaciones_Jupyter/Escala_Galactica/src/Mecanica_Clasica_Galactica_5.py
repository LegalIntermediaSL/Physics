import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 5)
y = np.cos(t + 5)
plt.plot(x, y)
plt.title('Simulation 5')
plt.show()
