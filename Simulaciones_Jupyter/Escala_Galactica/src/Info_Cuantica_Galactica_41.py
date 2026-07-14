import numpy as np
import matplotlib.pyplot as plt

def run_sim_41():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 41)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 41")
    plt.savefig("sim_41.png")

if __name__ == "__main__":
    run_sim_41()
