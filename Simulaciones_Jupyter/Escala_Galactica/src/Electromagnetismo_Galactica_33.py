import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 33)
    plt.plot(x, y)
    plt.title('Sim 33')
    plt.savefig('sim_33.png')

if __name__ == '__main__':
    run()
