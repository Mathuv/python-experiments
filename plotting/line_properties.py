import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Use keyword args
# plt.plot(x, y, linewidth=2.0)

# Use the setter methods
line, = plt.plot(x, y, '-')
line.set_antialiased(False)  # turn off antialising

plt.show()
