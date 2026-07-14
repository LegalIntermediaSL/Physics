import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 25)
y = np.cos(t + 25)
plt.plot(x, y)
plt.title('Simulation 25')
plt.show()
