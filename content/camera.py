# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np
from scipy import signal

def fastMeanBlur(image):
    
    O = image.copy()
    O = cv2.blur(image,(2,2))
    return O

def Otsu(image):
    otsuThe = 0
    maxval = 255
    otsuThe,des_Otsu = cv2.threshold(image,otsuThe,maxval,cv2.THRESH_OTSU)
    return des_Otsu


def CLAHE(image):
    clahe = cv2.createCLAHE(clipLimit = 2.0,tileGridSize = (4,4))
    O = clahe.apply(image)
    return O

def adaptiveThreshold(image,ksize):
    O = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,ksize,1)
    return O

def edgeDect(image,threshold1,threshold2):
    O = image.copy()
    O = cv2.Canny(image,threshold1,threshold2)
    return O

def circleDec(image):
    circles = cv2.HoughCircles(image,cv2.HOUGH_GRADIENT,1,100,200,param2 = 60,minRadius = 54)
    print(circles.shape)
    n = circles.shape[1]
    for i in xrange(n):
        center = (int(circles[0,i]),int(circles[0,i]))
        radius = circles[0,i]
        cv2.circle(image,center,radius,255,3)
    return image

def findContours(image):
    img = edgeDect(image,80,255)
    hc = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = hc[1]
    n = len(contours)
    contoursImg = np.zeros(img.shape,np.uint8)
    conImg_copy = contoursImg.copy()
    for i in xrange(n):
        cv2.drawContours(contoursImg,contours,i,255,1)
    rect = cv2.boundingRect(contours)
    cv2.imshow("img",contoursImg)
    


def imageProcess(image):
    img = fastMeanBlur(image)
    img = CLAHE(img)
    img = adaptiveThreshold(img,151)
    img = edgeDect(image,80,255)
   
    return img

if __name__ == "__main__":
    
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read()
   
    while(ret):
        cv2.imshow("camera",frame)
        findContours(frame[:,:,0])
        if cv2.waitKey(100) & 0xff == ord('q'):
            break
        ret,frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()
    
    



   
