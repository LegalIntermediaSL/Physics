import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    x = np.cos(t)
    y = np.sin(t)
    plt.plot(x, y)
    plt.title('Simulacion Galactica')

if __name__ == '__main__':
    run_sim()
