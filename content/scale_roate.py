# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:39:25 2018
实现图像的缩放，旋转，平移
warpAffine(src,M,dsize[,dst[,flags[,borderMode[,borderValue]]]])
	src:输入图像矩阵
	M:2*3的仿射变换矩阵
	dsize:输出图像的大小
	borderValue:?
@author: Administrator
"""

import cv2
import sys
import numpy as np
import math


if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python fileName.py imageFile"
    
    #图像的高、宽
    h,w = image.shape[:2]
    #缩小2倍
    A1 = np.array([[0.5,0,0],[0,0.5,0]],np.float32)
    d1 = cv2.warpAffine(image,A1,(w,h),borderValue = 125)
    #缩小两倍，在平移
    A2 = np.array([[0.5,0,w/4],[0,0.5,h/4]],np.float32)
    d2 = cv2.warpAffine(image,A2,(w,h),borderValue = 125)
    #在d2的基础上，绕图像的中心点旋转,缩放因子为0.2
    A3 = cv2.getRotationMatrix2D((w/2.0,h/2.0),30,0.2)
    d3 = cv2.warpAffine(d2,A3,(w,h),borderValue = 125)
   
cv2.imshow("image",image)
cv2.imshow("d1",d1)
cv2.imshow("d2",d2)
cv2.imshow("d3",d3)
cv2.waitKey(0)
cv2.destroyAllWindows()
