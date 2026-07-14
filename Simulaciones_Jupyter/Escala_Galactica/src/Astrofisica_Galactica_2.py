import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t + 2))
    plt.title("Simulation 2")
    plt.savefig("sim_2.png")

if __name__ == "__main__":
    run_sim()
