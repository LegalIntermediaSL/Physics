import numpy as np
import matplotlib.pyplot as plt

def run_sim_46():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 46)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 46")
    plt.savefig("sim_46.png")

if __name__ == "__main__":
    run_sim_46()
