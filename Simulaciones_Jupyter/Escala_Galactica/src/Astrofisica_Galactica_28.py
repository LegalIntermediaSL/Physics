import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t + 28))
    plt.title("Simulation 28")
    plt.savefig("sim_28.png")

if __name__ == "__main__":
    run_sim()
