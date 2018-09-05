# --*-- coding: utf-8 --*--
"""
自适应阈值处理：
	在对图像进行平滑处理时，均值平滑，高斯平滑，中值平滑
	用不同的规则计算结果作为每个像素设置阈值的参考。用于
	不均匀照明或者灰度值分布不均的情况
"""
import cv2
import sys

if __name__ == "__main__":
	if len(sys.argv) > 1:
		image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
	else:
		print "Usage:python adaptiveThreshold.py imagefile"
	cv2.imshow("image",image)
	#采用均值平滑处理策略
	O = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,1)
	cv2.imshow("O",O)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
