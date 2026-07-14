import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.title("Simulation")

if __name__ == "__main__":
    main()
