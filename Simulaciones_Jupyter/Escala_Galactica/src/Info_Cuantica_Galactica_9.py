import numpy as np
import matplotlib.pyplot as plt

def run_sim_9():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 9)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 9")
    plt.savefig("sim_9.png")

if __name__ == "__main__":
    run_sim_9()
