import numpy as np
import matplotlib.pyplot as plt

# evenly samples time at 200ms intervals
# np.range(Start, Stop, Step, DataType)
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()