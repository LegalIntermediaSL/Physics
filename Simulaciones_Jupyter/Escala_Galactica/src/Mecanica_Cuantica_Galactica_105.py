import numpy as np
import matplotlib.pyplot as plt

def simulate():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t))
    plt.savefig('sim_105.png')

if __name__ == "__main__":
    simulate()
