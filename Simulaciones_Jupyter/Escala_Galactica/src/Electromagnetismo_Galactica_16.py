import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 16)
    plt.plot(x, y)
    plt.title('Sim 16')
    plt.savefig('sim_16.png')

if __name__ == '__main__':
    run()
