import numpy as np
import matplotlib.pyplot as plt

def simulate():
    t = np.linspace(0, 10, 100)
    y = np.cos(t)
    plt.plot(t, y)
    plt.title("Galactic Simulation 65")
    plt.show()

if __name__ == "__main__":
    simulate()
