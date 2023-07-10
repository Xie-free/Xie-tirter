import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
import random

x = np.array([4, 5, 6])
h = np.array([4, 5, 6])
print(signal.convolve(x, h))  # 一维卷积运算

image = misc.face(gray=True)  # 二维图像数组, lena图像
shape = image.shape
w = np.zeros(shape)  # 全0二维数组, 卷积核
w[0][0] = 1.0
w[shape[0] - 1][shape[1] // 2] = 1.0
image_new = signal.fftconvolve(image, w)  # 使用FFT算法进行卷积
print(image_new.shape)

plt.figure()
plt.imshow(image_new)
plt.title("Filtered image")
plt.show()

x = np.arange(0, 100, 10)
print(random.shuffle(x))
print(x)
print(signal.medfilt(x, 3))