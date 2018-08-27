# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
腐蚀&膨胀：
	腐蚀：取邻域内的最大值
	膨胀：取邻域内的最小值
@author: Administrator
"""

import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python erode_dilate.py imageFile"
    cv2.imshow("image",image)
    #创建矩形结构元
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    #腐蚀图像，迭代次数采用默认值1
    r = cv2.erode(image,s)
    #边界提取
    e = image - r
    cv2.imshow("erode",r)
    cv2.imshow("edge",e)
    #结构元半径
    ra = 1
    MAX_R = 20
    cv2.namedWindow("dilate",1)
    def nothing(*arg):
        pass
    cv2.createTrackbar("r","dilate",ra,MAX_R,nothing)
    while True:
        ra = cv2.getTrackbarPos("r","dilate")
	#创建结构元
        s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2 * ra + 1, 2 * ra + 1))
        #膨胀图像
        d = cv2.dilate(image,s)
        cv2.imshow("dilate",d)
        ch = cv2.waitKey(5)
 	#按下Esc键退出循环
        if ch == 27:
            break
    cv2.destroyAllWindows()


   
