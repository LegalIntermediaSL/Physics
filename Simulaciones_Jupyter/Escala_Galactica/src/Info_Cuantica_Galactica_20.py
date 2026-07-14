import numpy as np
import matplotlib.pyplot as plt

def run_sim_20():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 20)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 20")
    plt.savefig("sim_20.png")

if __name__ == "__main__":
    run_sim_20()
