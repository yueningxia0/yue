import cv2
import  matplotlib.pyplot as plt

img_gray = cv2.imread("lenna.png",0)
hist_gray = cv2.equalizeHist(img_gray)

plt.subplot(221)
plt.hist(img_gray.ravel(),256)
plt.subplot(222)
plt.imshow(img_gray,cmap="gray")
plt.subplot(223)
plt.hist(hist_gray.ravel(),256)
plt.subplot(224)
plt.imshow(hist_gray,cmap="gray")
plt.show()
