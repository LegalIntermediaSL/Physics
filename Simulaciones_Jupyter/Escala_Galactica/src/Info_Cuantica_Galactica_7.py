import numpy as np
import matplotlib.pyplot as plt

def run_sim_7():
    x = np.linspace(0, 10, 100)
    y = np.sin(x + 7)
    plt.plot(x, y)
    plt.title("Galactic Quantum Info Simulation 7")
    plt.savefig("sim_7.png")

if __name__ == "__main__":
    run_sim_7()
