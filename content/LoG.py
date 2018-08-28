# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
高斯拉普拉斯边缘检测：
	相比用拉普拉斯核进行边缘检测，能减少卷积
	运算的次数，卷积核为高斯拉普拉斯卷积核
@author: Administrator
"""

import cv2
import numpy as np
from scipy import signal
import sys

#创建高斯拉普拉斯核
def createLoGKernel(sigma,size):
    H,W = size
    r,c = np.mgrid[0:H:1,0:W:1]
    r -= (H - 1) / 2
    c -= (W - 1) / 2
    sigma2 = pow(sigma,2.0)
    norm2 = np.power(r,2.0) + np.power(c,2.0)
    LoGKernel = (norm2 / sigma2 - 2) * np.exp(-norm2 / (2 * sigma2))
    return LoGKernel

#图像矩阵与高斯拉普拉斯核卷积
def LoG(image,sigma,size,_boundary = "symm"):
    loGKernel = createLoGKernel(sigma,size)
    img_conv_log = signal.convolve2d(image,loGKernel,"same",boundary = _boundary)
    return img_conv_log

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "Usage:python LoG.py imageFile"
    cv2.imshow("image",image)
    img_conv_log = LoG(image,6,(37,37),"symm")
    edge_binary = np.copy(img_conv_log)
    edge_binary[edge_binary > 0] = 255
    edge_binary[edge_binary <= 0] = 0
    edge_binary = edge_binary.astype(np.uint8)
    cv2.imshow("edge_binary",edge_binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
