import numpy as np
import matplotlib.pyplot as plt

def simulation():
    r = np.linspace(0.1, 10, 100)
    v = np.sqrt(1 / r)
    plt.plot(r, v)
    plt.title('Galactic Rotation Curve')
    plt.xlabel('Radius')
    plt.ylabel('Velocity')

if __name__ == '__main__':
    simulation()
