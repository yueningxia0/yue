import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import  rgb2gray

img = cv2.imread("lenna.png")  #读取图片
h,w = img.shape[:2]   #读取img的高，宽
img_gray = np.zeros([h,w],img.dtype)   #创建一个和img大小一样的画布，数组值为0

for i in range(h):
    for j in range(w):
        m = img[i,j]
        img_gray[i,j] = int(m[0]*0.11+m[1]*0.59+m[2]*0.3)

cv2.imshow("image gray",img_gray)   #展示图片

plt.subplot(131)
img = plt.imread("lenna.png")
plt.imshow(img)

plt.subplot(132)
img_gray = rgb2gray(img)
plt.imshow(img_gray,cmap='gray')

plt.subplot(133)

# img_binary = np.zeros([h,w],img.dtype)
# x,y = img_gray.shape[:2]
# for i in range(x):
#     for j in range(y):
#         if img_gray[i,j]>0.5:
#             img_binary[i,j] = 1
#         else:
#             img_binary[i,j] = 0

img_binary = np.where(img_gray>0.5,1,0)
plt.imshow(img_binary,cmap='gray')
plt.show()