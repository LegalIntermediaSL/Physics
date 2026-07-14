import numpy as np
import matplotlib.pyplot as plt

def run_sim_39():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 39)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 39")
    plt.savefig("sim_39.png")

if __name__ == "__main__":
    run_sim_39()
