import numpy as np
import  matplotlib.pyplot as plt
def entropy(p):
    return -p*np.log2(p)-(1-p)*np.log2(1-p)
p = np.linspace(0.01,0.99,100)

plt.plot(p,entropy(p))
plt.show()
