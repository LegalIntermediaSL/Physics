import numpy as np
import matplotlib.pyplot as plt

def run():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 45)
    plt.plot(x, y)
    plt.title('Sim 45')
    plt.savefig('sim_45.png')

if __name__ == '__main__':
    run()
