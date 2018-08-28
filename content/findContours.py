# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
外包、拟合轮廓
@author: Administrator
"""

import cv2
import numpy as np
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "Usage:python prewitt.py imageFile"
    #阈值化，生成二值图
    dst = cv2.GaussianBlur(img,(3,3),0.5)
    OtsuThresh = 0
    OtsuThresh,dst = cv2.threshold(dst,OtsuThresh,255,cv2.THRESH_OTSU)
    #形态学处理，消除细小白点
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    dst = cv2.morphologyEx(dst,cv2.MORPH_OPEN,s,iterations = 2)
    #寻找二值图轮廓，返回值是一个元组，hc[1]代表轮廓
    hc = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = hc[1]
    n = len(hc[1])
    contoursImg = np.zeros(img.shape,np.uint8)
    for i in xrange(n):
	#画出轮廓
        cv2.drawContours(contoursImg,contours,i,255,2)
	#画出轮廓的最小外包圆
        circle = cv2.minEnclosingCircle(contours[i])
        cv2.circle(img,(int(circle[0][0]),int(circle[0][1])),int(circle[1]),0,5)
	#多边形逼近
        approxCurve = cv2.approxPolyDP(contours[i],0.3,True)
        k = approxCurve.shape[0]
	#顶点连接，绘制多边形
        for i in xrange(k - 1):
            cv2.line(img,(approxCurve[i,0,0],approxCurve[i,0,1]),(approxCurve[i
                     +1,0,0],approxCurve[i + 1,0,1]),0,5)
	#首尾相接
        cv2.line(img,(approxCurve[k - 1,0,0],approxCurve[k - 1,0,1]),(approxCurve
                 [0,0,0],approxCurve[0,0,1]),0,5)
    cv2.imshow("contours",contoursImg)
    cv2.imshow("dst",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
