import numpy as np
import matplotlib.pyplot as plt

def run_sim_16():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 16)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 16")
    plt.savefig("sim_16.png")

if __name__ == "__main__":
    run_sim_16()
