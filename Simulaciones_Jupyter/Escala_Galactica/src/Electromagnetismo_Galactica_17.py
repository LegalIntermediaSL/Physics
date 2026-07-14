import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 17)
    plt.plot(x, y)
    plt.title('Sim 17')
    plt.savefig('sim_17.png')

if __name__ == '__main__':
    run()
