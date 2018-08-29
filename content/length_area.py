# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
轮廓的周长和面积:
	周长：arcLength
	面积：contourArea
@author: Administrator
"""

import cv2
import numpy as np

if __name__ == "__main__":
    #点集
    points = np.array([[[0,0]],[[50,30]],[[100,0]],[[100,100]]],np.float32)
    #计算点集所围区域的周长
    length1 = cv2.arcLength(points,False)	#首尾不相接
    length2 = cv2.arcLength(points,True)	#首尾相接
    area = cv2.contourArea(points)
    #计算点集所围成的区域的面积
    #打印周长和面积
    print length1,length2,area
