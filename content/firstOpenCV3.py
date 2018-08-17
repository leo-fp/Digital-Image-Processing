# -*- coding: utf-8 -*-
import cv2
import sys

if __name__ == "__main__":
	if len(sys.argv) > 1:
		#输入图像，第一个参数为图片路径，在OpenCV 2.x版本，第二个参数有所不同
		image = cv2.imread(sys.agrv[1],cv2.IMREAD_ANYCOLOR)
	else:
		print "Usage:python firstOpenCV3.py imageFile"
	
	
	#显示图像
	cv2.imshow("image",image)
	#最后两行实现按下任意键销毁窗口
	cv2.waitKey(0)
	cv2.destroyAllWindows()
