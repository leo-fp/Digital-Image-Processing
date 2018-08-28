# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
Prewitt边缘检测:
	Prewtt边缘检测算子由两个卷积核prewittx和prewitty构成
	图像与prewittx卷积可以反应图像垂直方向上的边缘，与
	prewitty卷积后可以反应图像水平方向上的边缘。prewittx
	算子可以分离成先对图像进行垂直方向上的非归一化的均值
	平滑，然后水平方向上的差分;而prewitty算子相反
@author: Administrator
"""

import cv2
import numpy as np
from scipy import signal
import sys

def prewitt(I,_boundary = "symm"):
    #垂直方向上的均值平滑
    ones_y = np.array([[1],[1],[1]],np.float32)
    i_conv_pre_x = signal.convolve2d(I,ones_y,mode = "same",boundary = _boundary)
    #水平方向上的差分
    diff_x = np.array([[1,0,-1]],np.float32)
    i_conv_pre_x = signal.convolve2d(i_conv_pre_x,diff_x,mode = "same",boundary = 
                                     _boundary)
    #水平方向上的均值平滑
    ones_x = np.array([[1,1,1]],np.float32)
    i_conv_pre_y = signal.convolve2d(I,ones_x,mode = "same",boundary = _boundary)
    #垂直方向上的差分
    diff_y = np.array([[1],[0],[-1]],np.float32)
    i_conv_pre_y = signal.convolve2d(i_conv_pre_y,diff_y,mode = "same",boundary =
                                     _boundary)
    return (i_conv_pre_x,i_conv_pre_y)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "Usage:python prewitt.py imageFile"
    #图像矩阵和两个Prewitt算子的卷积
    i_conv_pre_x,i_conv_pre_y = prewitt(image)
    abs_i_conv_pre_x = np.abs(i_conv_pre_x)
    abs_i_conv_pre_y = np.abs(i_conv_pre_y)
    edge_x = abs_i_conv_pre_x.copy()
    edge_y = abs_i_conv_pre_y.copy()
    edge_x[edge_x > 255] = 255
    edge_y[edge_y > 255] = 255
    edge_x = edge_x.astype(np.uint8)
    edge_y = edge_y.astype(np.uint8)
    cv2.imshow("edge_x",edge_x)
    cv2.imshow("edge_y",edge_y)
    #求边缘强度，有多种方式，这里使用的是插值法
    edge = 0.5 * abs_i_conv_pre_x + 0.5 * abs_i_conv_pre_y
    edge[edge > 255] = 255
    edge = edge.astype(np.uint8)
    cv2.imshow("edge",edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
