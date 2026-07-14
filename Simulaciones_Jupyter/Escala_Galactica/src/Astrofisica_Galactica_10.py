import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t + 10))
    plt.title("Simulation 10")
    plt.savefig("sim_10.png")

if __name__ == "__main__":
    run_sim()
