import numpy as np
import matplotlib.pyplot as plt

def run_sim_8():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 8)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 8")
    plt.savefig("sim_8.png")

if __name__ == "__main__":
    run_sim_8()
