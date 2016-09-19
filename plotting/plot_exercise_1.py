"""
Using matplotlib and numpy to create
a sine cusve and cosine curve
"""


import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace( -np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)

plt.show()