import numpy as np
import matplotlib.pyplot as plt

def run_sim_18():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 18)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 18")
    plt.savefig("sim_18.png")

if __name__ == "__main__":
    run_sim_18()
