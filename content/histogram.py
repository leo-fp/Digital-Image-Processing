# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
灰度直方图
@author: Administrator
"""
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python histogram.py imageFile"
    #图像矩阵的高、宽
    rows,cols = image.shape		
    #将二维的图像矩阵，变为一维的数组，便于计算灰度直方图    
    pixelSequence = image.reshape([rows*cols,])		
    numberBins = 256
    #计算灰度直方图
    histogram,bins,patch = plt.hist(pixelSequence,numberBins,facecolor = "black",
                                    histtype = "bar")
    #设置坐标轴的标签
    plt.xlabel(u"gray level")
    plt.ylabel(u"number of pixels")
    #设置坐标轴的范围
    y_maxValue = np.max(histogram)
    plt.axis([0,255,0,y_maxValue])
    plt.show()
   
