import numpy as np
import matplotlib.pyplot as plt

def run_sim_35():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 35)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 35")
    plt.savefig("sim_35.png")

if __name__ == "__main__":
    run_sim_35()
