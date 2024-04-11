import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lenna.png",0)  #读取灰度图片
x = cv2.Sobel(img,cv2.CV_16S,1,0,ksize=3)  #计算水平方向的导数
y = cv2.Sobel(img,cv2.CV_16S,0,1,ksize=3)  #计算垂直方向的导数
xy = cv2.addWeighted(x,0.5,y,0.5,gamma=0)

sobel_x = cv2.convertScaleAbs(x)
sobel_y = cv2.convertScaleAbs(y)
sobel_xy = cv2.convertScaleAbs(xy)

plt.subplot(131)
plt.imshow(sobel_x,cmap="gray")
plt.subplot(132)
plt.imshow(sobel_y,cmap="gray")
plt.subplot(133)
plt.imshow(sobel_xy,cmap="gray")
plt.show()

# cv2.imshow("sobel x",sobel_x)
# cv2.imshow("sobel y",sobel_y)
# cv2.imshow("sobel xy",sobel_xy)
# cv2.waitKey(0)