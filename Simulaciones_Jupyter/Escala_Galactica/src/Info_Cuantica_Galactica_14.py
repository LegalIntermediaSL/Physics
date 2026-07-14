import numpy as np
import matplotlib.pyplot as plt

def run_sim_14():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 14)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 14")
    plt.savefig("sim_14.png")

if __name__ == "__main__":
    run_sim_14()
