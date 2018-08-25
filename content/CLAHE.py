# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
限制对比度的自适应直方图均衡化:
	将原图像分成不重叠的区域块，然后使区域内的灰度直方图变平
	过程中，对超过一定限制的直方图进行裁剪，并均匀分配到该区
	域，避免了噪声的出现
@author: Administrator
"""

import cv2
import sys
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) > 1:
        src = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python CLAHE.py imageFile"
    #创建CLAHE对象
    clahe = cv2.createCLAHE(clipLimit = 2.0,tileGridSize = (8,8))
    #限制对比度的自适应阈值均衡化
    dst = clahe.apply(src)
    cv2.imshow("src",src)
    cv2.imshow("clahe",dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   
