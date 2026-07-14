import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 47)
y = np.cos(t + 47)
plt.plot(x, y)
plt.title('Simulation 47')
plt.show()
