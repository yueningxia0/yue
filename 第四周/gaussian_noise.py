import cv2
import random
from skimage import util
import numpy as np

def gaussianNoise(img,sigma,mu,percent):
    h,w = img.shape[:2]
    img = img.astype(np.uint32)
    imgOut = img
    noiseNum = int(h*w*percent)
    for i in range(noiseNum):
        randh = random.randint(0,h-1)  #随机生成0到h-1的数
        randw = random.randint(0,w-1)
        imgOut[randh,randw] = imgOut[randh,randw] + random.gauss(mu,sigma)  # pout = pin + random.guass
        if imgOut[randh,randw] > 255:
            imgOut[randh,randw] = 255
        elif imgOut[randh,randw] < 0:
            imgOut[randh, randw] = 0
    imgOut = imgOut.astype(np.uint8)
    return imgOut

if __name__ == '__main__':
    image = cv2.imread("lenna.png",0) # 读取灰度图片
    imageOut = gaussianNoise(image,10,2,0.8)
    image = cv2.imread("lenna.png")
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    noise_gauss = util.random_noise(image_gray,mode="gaussian")

    cv2.imshow("gauss",imageOut)
    cv2.imshow("src",image_gray)
    cv2.imshow("noise_gauss",noise_gauss)
    cv2.waitKey(0)
