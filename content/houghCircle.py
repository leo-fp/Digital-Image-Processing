# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
基于梯度的霍夫圆检测
@author: Administrator
"""

import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "Usage:python houghCircle.py imageFile"
    circles = cv2.HoughCircles(image,cv2.HOUGH_GRADIENT,1,100,200,param2 = 60,
                               minRadius = 54)
    print type(circles)
    print circles.shape
    #圆的个数
    n = circles.shape[1]
    for i in xrange(n):
	#圆心
        center = (int(circles[0,i,0]),int(circles[0,i,1]))
        radius = circles[0,i,2]
        cv2.circle(image,center,radius,255,3)
    cv2.imshow("src",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
