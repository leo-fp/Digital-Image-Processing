# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
快速均值平滑：
	利用矩阵的积分，可以求出矩阵中任意区域的和，
	然后求均值，openCV提供了blur和boxFilter两个
	函数来实现该功能
以下为blur函数实例
@author: Administrator
"""

import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python fastMeanBlur.py imageFile"
    cv2.imshow("image",image)
    O = image.copy()
    O = cv2.blur(image,(3,5))
    cv2.imshow("O",O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


   
