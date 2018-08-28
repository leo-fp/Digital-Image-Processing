# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
查找、绘制轮廓
@author: Administrator
"""

import cv2
import numpy as np
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "Usage:python draw.py imageFile"
    img = cv2.GaussianBlur(img,(3,3),0.5)
    binaryImg = cv2.Canny(img,50,200)
    cv2.imshow("binary",binaryImg)
    #边缘的轮廓，返回的contours是一个list列表
    hc = cv2.findContours(binaryImg,cv2.RETR_EXTERNAL,cv2.
                                  CHAIN_APPROX_SIMPLE) 
    contours = hc[1]
    print type(contours)
    print contours[0].shape
    n = len(contours)
    contoursImg = []
    #画出吵到的轮廓
    for i in xrange(n):
	#画出黑色画布
        temp = np.zeros(binaryImg.shape,np.uint8)
        contoursImg.append(temp)
        #在第i个黑色画布上，画第i个轮廓
        cv2.drawContours(contoursImg[i],contours,i,255,2)
        cv2.imshow("contour_" + str(i),contoursImg[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
