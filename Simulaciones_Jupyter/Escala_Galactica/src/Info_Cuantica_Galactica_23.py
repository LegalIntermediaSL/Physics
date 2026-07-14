import numpy as np
import matplotlib.pyplot as plt

def run_sim_23():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 23)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 23")
    plt.savefig("sim_23.png")

if __name__ == "__main__":
    run_sim_23()
