import numpy as np
import matplotlib.pyplot as plt

def run_sim_22():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 22)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 22")
    plt.savefig("sim_22.png")

if __name__ == "__main__":
    run_sim_22()
