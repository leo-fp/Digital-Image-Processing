# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
点和轮廓的关系:
	double pointPolygonTest(InputArray contour,Point2f pt, bool measureDist)
	contour:输入的点集
	pt:坐标点
	measureDist:是否计算坐标点到轮廓的距离
	返回值+1、0、-1分别代表在轮廓内、轮廓上、轮廓外
@author: Administrator
"""

import cv2
import numpy as np

contour = np.array([[0,0],[50,30],[100,100],[100,0]],np.float32)
dist1 = cv2.pointPolygonTest(contour,(80,40),False)
dist2 = cv2.pointPolygonTest(contour,(50,0),False)
dist3 = cv2.pointPolygonTest(contour,(40,80),False)
print dist1,dist2,dist3  
    
