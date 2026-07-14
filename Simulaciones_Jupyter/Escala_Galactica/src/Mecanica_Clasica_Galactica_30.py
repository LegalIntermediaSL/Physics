import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 30)
y = np.cos(t + 30)
plt.plot(x, y)
plt.title('Simulation 30')
plt.show()
