import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 19)
    plt.plot(x, y)
    plt.title('Sim 19')
    plt.savefig('sim_19.png')

if __name__ == '__main__':
    run()
