# -*- coding: utf-8 -*-
"""
Created on Sun Sep 02 21:43:48 2018
调用摄像头显示图像
@author: Administrator
"""

import cv2

cap = cv2.VideoCapture(0)	#创建对象
success,frame = cap.read()	#如果读取到画面数据则success为True
while(success):
    cv2.imshow("camera",frame)
    if cv2.waitKey(100) & 0xff == ord('q'):	#画面持续时间为100ms，如果在等待时间内按下了q键则退出循环
        break
    success,frame = cap.read()
cap.release()				
cv2.destroyAllWindows()		#销毁窗口
