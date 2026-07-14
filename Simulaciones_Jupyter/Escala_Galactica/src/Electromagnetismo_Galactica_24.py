import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 24)
    plt.plot(x, y)
    plt.title('Sim 24')
    plt.savefig('sim_24.png')

if __name__ == '__main__':
    run()
