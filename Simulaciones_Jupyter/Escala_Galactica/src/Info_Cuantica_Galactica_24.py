import numpy as np
import matplotlib.pyplot as plt

def run_sim_24():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 24)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 24")
    plt.savefig("sim_24.png")

if __name__ == "__main__":
    run_sim_24()
