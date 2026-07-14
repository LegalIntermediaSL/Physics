import numpy as np
import matplotlib.pyplot as plt

def run_sim_4():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 4)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 4")
    plt.savefig("sim_4.png")

if __name__ == "__main__":
    run_sim_4()
