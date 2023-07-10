import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 10, size=8)
y = np.random.randint(5, 15, size=8)
plt.scatter(x, y)
for i in range(len(x)):
    plt.text(x[i], y[i] + 0.3, y[i])
plt.show()
