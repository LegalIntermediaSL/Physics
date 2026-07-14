import numpy as np
import matplotlib.pyplot as plt

def run_sim_17():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 17)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 17")
    plt.savefig("sim_17.png")

if __name__ == "__main__":
    run_sim_17()
