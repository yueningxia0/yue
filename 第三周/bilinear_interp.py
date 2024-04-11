import cv2
import numpy as np

def function(src_img,dh,dw):
    sh,sw,c = src_img.shape
    dst_img = np.zeros((dh,dw,c),dtype=np.uint8)
    scale_h,scale_w = sh/dh,sw/dw
    if dh==sh and dw==sw:
        return src_img.copy()
    for i in range(c):
        for m in range(dh):
            for n in range(dw):
                src_x = (m+0.5)*scale_h-0.5
                src_y = (n+0.5)*scale_w-0.5

                src_x0 = int(src_x)
                src_x1 = min(sh-1,src_x0+1)
                src_y0 = int(src_y)
                src_y1 = min(sw - 1, src_y0 + 1)
                temp0 = (src_x1-src_x)* src_img[src_x0,src_y0,i]+(src_x-src_x0)*src_img[src_x1,src_y0,i]
                temp1 = (src_x1-src_x)* src_img[src_x0,src_y1,i]+(src_x-src_x0)*src_img[src_x1,src_y1,i]

                dst_img[m,n,i] = (src_y1-src_y)*temp0+(src_y-src_y0)*temp1
    return dst_img

if __name__ == '__main__':
    src_img = cv2.imread("lenna.png")
    dh,dw = 800,800
    dst_img = function(src_img,dh,dw)
    cv2.imshow("bilinear interp",dst_img)
    cv2.waitKey(0)