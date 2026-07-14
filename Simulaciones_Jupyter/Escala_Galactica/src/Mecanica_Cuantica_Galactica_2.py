import numpy as np
import matplotlib.pyplot as plt

def simulate():
    x = np.linspace(-10, 10, 1000)
    psi = np.exp(-x**2 / 2) * np.exp(1j * 5 * x)
    plt.plot(x, np.abs(psi)**2)
    plt.title("Quantum Simulation 2")
    plt.xlabel("x")
    plt.ylabel("|psi|^2")

if __name__ == "__main__":
    simulate()
