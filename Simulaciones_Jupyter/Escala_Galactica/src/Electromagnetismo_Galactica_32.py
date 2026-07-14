import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 32)
    plt.plot(x, y)
    plt.title('Sim 32')
    plt.savefig('sim_32.png')

if __name__ == '__main__':
    run()
