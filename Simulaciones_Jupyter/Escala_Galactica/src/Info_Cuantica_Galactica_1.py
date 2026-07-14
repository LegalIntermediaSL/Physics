import numpy as np
import matplotlib.pyplot as plt

def run_sim_1():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 1)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 1")
    plt.savefig("sim_1.png")

if __name__ == "__main__":
    run_sim_1()
