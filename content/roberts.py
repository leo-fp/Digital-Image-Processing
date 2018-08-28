# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
Roberts边缘检测：
	Roberts边缘检测是图像分别与两个卷积核分别做卷积，然后
	用一定的方法来计算输出的边缘强度(这里用的是取对应位置
	平方和的开方),因roberts边缘检测使用了很少的邻域像素来
	近似边缘强度，所以对图像中的噪声具有高度敏感性。
@author: Administrator
"""

import cv2
import sys
import numpy as np
from scipy import signal
    
def roberts(I,_boundary = 'fill',_fillvalue = 0):
    #图像的高、宽
    H1,W1 = I.shape[0:2]
    #卷积核的尺寸
    H2,W2 = 2,2
    #卷积核1及锚点位置
    R1 = np.array([[1,0],[0,-1]],np.float32)
    kr1,kc1 = 0,0
    #计算full卷积
    IconR1 = signal.convolve2d(I,R1,mode = "full",boundary = _boundary,fillvalue = 
                               _fillvalue)
    #取same卷积
    IconR1 = IconR1[H2 - kr1 - 1:H1 + H2 - kr1 - 1,W2 - kc1 - 1:W1 + W2 - kc1 - 1]
    #卷积核2
    R2 = np.array([[0,1],[-1,0]],np.float32)
    #full卷积
    IconR2 = signal.convolve2d(I,R2,mode = "full",boundary = _boundary,fillvalue=
                               _fillvalue)
    #锚点位置 
    kr2,kc2 = 0,1
    #same卷积
    IconR2 = IconR2[H2 - kr2 - 1:H1 + H2 - kr2 -1,W2 - kc2 - 1:W1 + W2 - kc2 - 1] 
    return (IconR1,IconR2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python roberts.py imageFile"
    cv2.imshow("image",image)
    IconR1,IconR2 = roberts(image,'symm')
    IconR1 = np.abs(IconR1)
    edge_45 = IconR1.astype(np.uint8)
    cv2.imshow("edge_45",edge_45)
    IconR2 = np.abs(IconR2)
    edge_135 = IconR2.astype(np.uint8)
    cv2.imshow("edge_135",edge_135)
    edge = np.sqrt(np.power(IconR1,2.0) + np.power(IconR2,2.0))
    edge = np.round(edge)
    edge[edge > 255] = 255
    edge = edge.astype(np.uint8)
    cv2.imshow("edge",edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

   
