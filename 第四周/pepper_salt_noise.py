import cv2
import random

def pepperSaltNoise(img,percent):
    h,w = img.shape[:2]
    noiseNum = int(h*w*percent)
    imgOut = img
    for i in range(noiseNum):
        randh = random.randint(0,h-1)
        randw = random.randint(0,w-1)

        if random.random() > 0.5:
            imgOut[randh,randw] = 255
        else:
            imgOut[randh,randw] = 0
    return imgOut

if __name__ == '__main__':
    img = cv2.imread("lenna.png")
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.imread("lenna.png",0)
    img_noise = pepperSaltNoise(img,0.2)
    cv2.imshow("noise",img_noise)
    cv2.imshow("src",img_gray)
    cv2.waitKey(0)