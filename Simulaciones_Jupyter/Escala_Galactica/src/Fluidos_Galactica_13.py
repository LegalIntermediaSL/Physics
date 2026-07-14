import numpy as np
import matplotlib.pyplot as plt

def sim_13():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Simulation 13')
    plt.show()

if __name__ == '__main__':
    sim_13()
