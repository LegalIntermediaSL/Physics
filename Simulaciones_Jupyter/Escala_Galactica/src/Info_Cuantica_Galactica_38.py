import numpy as np
import matplotlib.pyplot as plt

def run_sim_38():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 38)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 38")
    plt.savefig("sim_38.png")

if __name__ == "__main__":
    run_sim_38()
