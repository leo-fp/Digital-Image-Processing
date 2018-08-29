# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
轮廓的凸包缺陷:
	求轮廓上的点到凸包的距离
@author: Administrator
"""

import cv2
import numpy as np
#轮廓
contour = np.array([[20,20],[50,70],[20,120],[120,120],[100,70],[120,20]],np.int32)
#轮廓的凸包
hull = cv2.convexHull(contour,returnPoints = False)
defects = cv2.convexityDefects(contour,hull)
#打印凸包
print hull
#打印凸包缺陷
print defects
