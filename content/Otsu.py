# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
Otsu阈值处理:
	自动选取能使前景区域的平均灰度，背景区域的平均灰度与
	整体图像的平均灰度方差最大的阈值
@author: Administrator
"""

import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python Ostu.py imageFile"
    cv2.imshow("image",image)
    otsuThe = 0
    maxval = 255
    #ostuThe为选取的阈值
    otsuThe,des_Otsu = cv2.threshold(image,otsuThe,maxval,cv2.THRESH_OTSU) 
    cv2.imshow("des",des_Otsu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


   
