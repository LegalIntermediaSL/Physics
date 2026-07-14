import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t + 6))
    plt.title("Simulation 6")
    plt.savefig("sim_6.png")

if __name__ == "__main__":
    run_sim()
