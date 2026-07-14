import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 9)
y = np.cos(t + 9)
plt.plot(x, y)
plt.title('Simulation 9')
plt.show()
