import numpy as np
import matplotlib.pyplot as plt
def sim():
    plt.plot(np.random.rand(100))
    plt.savefig('out.png')
if __name__=='__main__': sim()
