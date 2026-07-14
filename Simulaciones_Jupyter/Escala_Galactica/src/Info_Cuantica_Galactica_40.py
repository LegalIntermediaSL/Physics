import numpy as np
import matplotlib.pyplot as plt

def run_sim_40():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 40)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 40")
    plt.savefig("sim_40.png")

if __name__ == "__main__":
    run_sim_40()
