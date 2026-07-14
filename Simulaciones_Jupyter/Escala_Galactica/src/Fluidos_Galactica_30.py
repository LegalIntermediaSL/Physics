import numpy as np
import matplotlib.pyplot as plt

def sim_30():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Simulation 30')
    plt.show()

if __name__ == '__main__':
    sim_30()
