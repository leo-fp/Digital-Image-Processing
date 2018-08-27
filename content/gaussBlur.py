# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
高斯平滑
原理：用高斯矩阵归一化后得高斯卷积算子与原图进行卷积。
      因高斯卷积算子是可分离的卷积核,所以可以分两次对
      图像进行卷积，一次用水平方向上的卷积核，一次用
      垂直方向上的卷积核
方法1：blurImage = cv2.GaussianBlur(image,(51,51),5,blurImage,5)
方法2:如下

@author: Administrator
"""

import cv2
import sys
import numpy as np
import math
from scipy import signal

#构建高斯矩阵
def getGaussKernel(sigma,H,W):
    gaussMatrix = np.zeros([H,W],np.float32)
    #得到中心点位置
    cH = (H - 1) / 2
    cW = (W - 1) / 2
    #计算gauss(sigma,r,c)
    for r in xrange(H):
        for c in xrange(W):
            norm2 = math.pow(r - cH,2) + math.pow(c - cW,2)
            gaussMatrix[r][c] = math.exp(-norm2 / (2 * math.pow(sigma,2)))
    #计算高斯矩阵和
    sumGm = np.sum(gaussMatrix)
    #归一化
    gaussKernel = gaussMatrix / sumGm
    return gaussKernel

def gaussBlur(image,sigma,H,W,_boundary = "fill",_fillvalue = 0):
    #构建水平方向上的高斯卷积核
    gausskenrnel_x = cv2.getGaussianKernel(sigma,W,cv2.CV_64F)
    #转置 
    gaussKenrnel_x = np.transpose(gausskenrnel_x)
    #图像矩阵与水平高斯核卷积
    gaussBlur_x = signal.convolve2d(image,gaussKenrnel_x,mode = "same",boundary
                                    = _boundary,fillvalue = _fillvalue)
    #构建垂直方向上的高斯卷积核
    gaussKenrnel_y = cv2.getGaussianKernel(sigma,H,cv2.CV_64F)
    #与垂直方向上的高斯核卷积
    gaussBlur_xy = signal.convolve2d(gaussBlur_x,gaussKenrnel_y,mode = "same",
                                     boundary = _boundary,fillvalue = _fillvalue)
    return gaussBlur_xy

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python gaussBlur.py imageFile"
    cv2.imshow("image",image)
    #高斯平滑
    blurImage = gaussBlur(image,5,51,51,"symm")
    #对blurImage进行灰度级显示
    blurImage = np.round(blurImage)
    blurImage = blurImage.astype(np.uint8)
    cv2.imshow("GaussBlur",blurImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


   
