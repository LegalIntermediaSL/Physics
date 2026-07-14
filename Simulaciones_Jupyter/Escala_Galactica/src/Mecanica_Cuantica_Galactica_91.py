import numpy as np
import matplotlib.pyplot as plt

def run_simulation():
    t = np.linspace(0, 10, 100)
    y = np.sin(t)
    plt.plot(t, y)
    plt.title("Galactic Quantum Mechanics Simulation 91")
    plt.show()

if __name__ == "__main__":
    run_simulation()
