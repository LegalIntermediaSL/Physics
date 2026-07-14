import numpy as np
import matplotlib.pyplot as plt

def run_sim_10():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 10)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 10")
    plt.savefig("sim_10.png")

if __name__ == "__main__":
    run_sim_10()
