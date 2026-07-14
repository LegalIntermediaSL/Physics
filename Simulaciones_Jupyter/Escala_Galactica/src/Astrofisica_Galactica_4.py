import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t + 4))
    plt.title("Simulation 4")
    plt.savefig("sim_4.png")

if __name__ == "__main__":
    run_sim()
