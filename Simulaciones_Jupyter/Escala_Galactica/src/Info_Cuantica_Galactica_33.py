import numpy as np
import matplotlib.pyplot as plt

def run_sim_33():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 33)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 33")
    plt.savefig("sim_33.png")

if __name__ == "__main__":
    run_sim_33()
