import cv2
import numpy as np

def function(img,nh,nw):
    h,w,c = img.shape   #放大缩小不能改变通道数
    nimg = np.zeros([nh,nw,c],img.dtype)
    sh = nh/h
    sw = nw/w
    for i in range(nh):
        for j in range(nw):
            x = int(i/sh+0.5)
            y = int(j/sw+0.5)
            nimg[i,j] = img[x,y]
    return nimg

img = cv2.imread("lenna.png")
nimg = function(img,800,800)
cv2.imshow("image",img)
cv2.imshow("nearest interp",nimg)
cv2.waitKey(0)
