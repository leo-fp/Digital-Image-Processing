# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
直方图正规化
原理：
	直方图正规化是一种自动选取a和b的线性变换方法，其中
	a = (Omax - Omin) / (Imax - Imin)
	b = Omax - (Omax - Omin) / (Imax - Imin) * Imin

@author: Administrator
"""

import cv2
import sys
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) > 1:
        I = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python normlize.py imageFile"
    Imax = np.max(I)
    Imin = np.min(I)
    Omin,Omax = 0,255
    a = float(Omax - Omin) / (Imax - Imin)
    b = Omin - a * Imin
    O = a * I + b
    O = O.astype(np.uint8)
    
    cv2.imshow("I",I)
    cv2.imshow("O",O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   
