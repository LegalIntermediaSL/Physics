import numpy as np
import matplotlib.pyplot as plt

def run_simulation():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Simulacion Electromagnetismo Galactica 70')
    plt.xlabel('X')
    plt.ylabel('Y')
    print('Simulation 70 ran.')

if __name__ == '__main__':
    run_simulation()
