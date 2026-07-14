import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 27)
y = np.cos(t + 27)
plt.plot(x, y)
plt.title('Simulation 27')
plt.show()
