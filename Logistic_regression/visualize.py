import matplotlib.pyplot as plt
from ml.data import *

fig = plt.figure()

ax = fig.add_subplot(111)
x, y = load_chips_dataset()

red = 1
blue = 0

x1 = []
y1 = []
x2 = []
y2 = []
for i in range(len(x)):
    if y[i] > 0:
        x1.append(x[i][0])
        y1.append(x[i][1])
    else:
        x2.append(x[i][0])
        y2.append(x[i][1])

ax.plot(x1, y1, 'bo')
ax.plot(x2, y2, 'ro')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('chips.txt')
plt.show()
