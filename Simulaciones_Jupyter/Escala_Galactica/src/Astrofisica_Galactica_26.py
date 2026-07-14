import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t + 26))
    plt.title("Simulation 26")
    plt.savefig("sim_26.png")

if __name__ == "__main__":
    run_sim()
