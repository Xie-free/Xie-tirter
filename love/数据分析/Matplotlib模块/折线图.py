import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
x = ["1-3", "4-6", "7-9", "10-12"]
y = [257, 301, 428, 475]
plt.plot(x, y)
plt.scatter(x, y)
plt.xlabel("季度")
plt.ylabel("销售额")
for i in range(len(x)):
    plt.text(x[i], y[i], y[i])
plt.show()
