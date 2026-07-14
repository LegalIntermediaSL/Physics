import numpy as np
import matplotlib.pyplot as plt

def run_sim_45():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 45)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 45")
    plt.savefig("sim_45.png")

if __name__ == "__main__":
    run_sim_45()
