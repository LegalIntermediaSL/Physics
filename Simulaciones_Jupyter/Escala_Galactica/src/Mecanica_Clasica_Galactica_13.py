import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 100)
x = np.sin(t + 13)
y = np.cos(t + 13)
plt.plot(x, y)
plt.title('Simulation 13')
plt.show()
