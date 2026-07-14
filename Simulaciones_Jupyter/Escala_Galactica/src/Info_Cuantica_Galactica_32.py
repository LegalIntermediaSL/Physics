import numpy as np
import matplotlib.pyplot as plt

def run_sim_32():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 32)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 32")
    plt.savefig("sim_32.png")

if __name__ == "__main__":
    run_sim_32()
