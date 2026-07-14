import numpy as np
import matplotlib.pyplot as plt

def run_sim_21():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 21)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 21")
    plt.savefig("sim_21.png")

if __name__ == "__main__":
    run_sim_21()
