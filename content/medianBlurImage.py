# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
中值平滑：
	对邻域中的像素点按灰度值进行排序，然后选择该组
	中的中值作为输出的灰度值，最重要的能力是去除椒
	盐噪声,openCV提供medianBlur函数实现该功能
@author: Administrator
"""

import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python gaussBlur.py imageFile"
    cv2.imshow("image",image)
    medianBlurImage = cv2.medianBlur(image,5)
    cv2.imshow("medianBlurImage",medianBlurImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


   
