import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 23)
y = np.cos(t + 23)
plt.plot(x, y)
plt.title('Simulation 23')
plt.show()
