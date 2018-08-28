# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
Canny边缘检测:
	需要两个阈值，一个低阈值，一个高阈值，选定
	边缘强度大于高阈值的点，剔除边缘强度小于低
	阈值的点，然后在边缘强度大于低阈值的情况下
	尽可能延长边缘。	
@author: Administrator
"""

import cv2
import numpy as np
from scipy import signal
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "Usage:python canny.py imageFile"
    O = image.copy()
    O = cv2.Canny(image,10,250)
    cv2.imshow("o",O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
