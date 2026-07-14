import numpy as np
import matplotlib.pyplot as plt

def sim():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Simulacion Electromagnetismo')

if __name__ == '__main__':
    sim()
