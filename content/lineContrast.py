# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:53:29 2018
原理：假设输入图像为I，宽为W,高为H，输出图像记为O
	O(r,c) = a * I(r,c) + b, 0 <= r < H, 0 <= c < W
	通过调整a，b实现拉伸(a > 1)或压缩(a < 1)图像的灰度级范围
@author: Administrator
"""
import cv2
import sys
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python lineContrast.py imageFile"
    
    a = 2
    o = float(a)*image
    o[o > 255] = 255
    o = np.round(o)		#浮点数四舍五入
    o = o.astype(np.uint8)	#改变ndarry的数据类型
    cv2.imshow("image",image)
    cv2.imshow("o",o)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   
