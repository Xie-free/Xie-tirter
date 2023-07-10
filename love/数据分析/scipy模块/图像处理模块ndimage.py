from scipy import misc
from scipy import ndimage
import matplotlib.pyplot as plt

face = misc.face()  # face是测试图像之一
plt.figure()  # 创建图像
plt.imshow(face)  # 绘制测试图像
plt.show()  # 原始图像

blurred_face = ndimage.gaussian_filter(face, sigma=7)  # 高斯滤波
plt.imshow(blurred_face)
plt.show()

blurred_face1 = ndimage.gaussian_filter(face, sigma=1)  # 边缘锐化
blurred_face3 = ndimage.gaussian_filter(face, sigma=3)
shape_face = blurred_face3 + 6 * (blurred_face3 - blurred_face1)
plt.imshow(shape_face)
plt.show()