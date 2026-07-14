import numpy as np
import matplotlib.pyplot as plt

def run_sim_5():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 5)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 5")
    plt.savefig("sim_5.png")

if __name__ == "__main__":
    run_sim_5()
