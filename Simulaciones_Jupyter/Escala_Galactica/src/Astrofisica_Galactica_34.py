import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t + 34))
    plt.title("Simulation 34")
    plt.savefig("sim_34.png")

if __name__ == "__main__":
    run_sim()
