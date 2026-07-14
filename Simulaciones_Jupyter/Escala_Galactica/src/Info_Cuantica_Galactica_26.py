import numpy as np
import matplotlib.pyplot as plt

def run_sim_26():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 26)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 26")
    plt.savefig("sim_26.png")

if __name__ == "__main__":
    run_sim_26()
