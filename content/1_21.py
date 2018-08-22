# -*- coding: utf-8 -*-
"""
将RGB彩色图转换为三维的ndarry，消除红色部分后合并图像
"""
import numpy as np
import cv2
import sys

if __name__ == "__main__":
	if len(sys.argv) > 1:
		#输入图像，第一个参数为图片路径，在OpenCV 2.x版本，第二个参数有所不同
		image = cv2.imread(sys.agrv[1],cv2.IMREAD_COLOR)
	else:
		print "Usage:python firstOpenCV3.py imageFile"
	
	#彩色图像分离通道	
	b = image[:,:,2]
	g = image[:,:,1]
	r = image[:,:,0]

	#初始化一个全零阵，大小和输入图像大小一致
	r_new = np.zeros((image.shape[0],image.shape[1]),dtype = image.dtype)
	img_without_red = np.dstack([b,g,r_new])	#合并通道
	#显示图像
	cv2.imshow("b",b)
	cv2.imshow("g",g)
	cv2.imshow("r",r)
	cv2.imshow("img_new",img_without_red)

	#最后两行实现按下任意键销毁窗口
	cv2.waitKey(0)
	cv2.destroyAllWindows()
