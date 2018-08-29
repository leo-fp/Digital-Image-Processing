# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
快速傅里叶变换检测:
	用cv2.getOptimalDFTSize(int vecsize)函数将图像
	扩展至某一规模后，能降低傅里叶变换的时间复杂度
	将原图与最后还原的图像的差检测两者是否有效
@author: Administrator
"""

import cv2
import numpy as np
import sys

def fft2Image(src):
    r,c = src.shape[:2]
    #得到快速傅里叶变换的最优扩充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    fft2 = np.zeros((rPadded,cPadded,2),np.float32)
    fft2[:r,:c,0] = src
    #快速傅里叶变换
    cv2.dft(fft2,fft2,cv2.DFT_COMPLEX_OUTPUT)
    return fft2

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python fft2.py imageFile"
    fft2 = fft2Image(image)
    #傅里叶逆变换
    ifft2 = np.zeros(fft2.shape[:2],np.float32)
    cv2.dft(fft2,ifft2,cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)
    img = np.copy(ifft2[:image.shape[0],:image.shape[1]])
    #通过判断原矩阵减去逆变换裁剪后的矩阵是否为零矩阵，验证两者是否相同
    print np.max(image - img)
