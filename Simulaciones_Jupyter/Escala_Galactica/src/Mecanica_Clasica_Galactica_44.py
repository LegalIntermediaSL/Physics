import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 44)
y = np.cos(t + 44)
plt.plot(x, y)
plt.title('Simulation 44')
plt.show()
