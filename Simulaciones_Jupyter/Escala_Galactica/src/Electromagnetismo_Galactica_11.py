import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 11)
    plt.plot(x, y)
    plt.title('Sim 11')
    plt.savefig('sim_11.png')

if __name__ == '__main__':
    run()
