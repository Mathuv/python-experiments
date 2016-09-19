import matplotlib.pyplot as plt

# plt.plot([1,2,3,4])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# format string
# defaut 'b-' - solid blue line
# 'ro' - red circles
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') # 'ro' is a format string
# axix [xmin, xmax, ymin, ymax] - specifies the viewpoint of the axxis
plt.axis([0, 6, 0, 20])
plt.ylabel('Some numbers')
plt.show()