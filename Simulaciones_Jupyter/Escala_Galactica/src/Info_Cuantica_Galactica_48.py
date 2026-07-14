import numpy as np
import matplotlib.pyplot as plt

def run_sim_48():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 48)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 48")
    plt.savefig("sim_48.png")

if __name__ == "__main__":
    run_sim_48()
