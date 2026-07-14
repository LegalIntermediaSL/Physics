import numpy as np
import matplotlib.pyplot as plt

def run_sim():
    t = np.linspace(0, 10, 100)
    plt.plot(t, np.sin(t + 43))
    plt.title("Simulation 43")
    plt.savefig("sim_43.png")

if __name__ == "__main__":
    run_sim()
