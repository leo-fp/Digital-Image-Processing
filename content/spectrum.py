# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
傅里叶变换的幅度谱(傅里叶谱)和相位谱计算方法和灰度级显示:
	设图像I进行傅里叶变换后得到复数矩阵F,幅度谱为实部
	与虚部的平方和。相位谱为虚部与实部的比值的反正切值。
	因为幅度谱的最大值在左上角，为了便于观察，通常在
	傅里叶变换之前将图像矩阵乘以(-1)^(r + c)。
@author: Administrator
"""

import cv2
import numpy as np
import sys
import math

#幅度谱
def amplitudeSpectrum(fft2):
    real2 = np.power(fft2[:,:,0],2.0)
    Imag2 = np.power(fft2[:,:,1],2.0)
    amplitude = np.sqrt(real2 + Imag2)
    return amplitude

#灰度值转换
def graySpectrum(amplitude):
    amplitude = np.log(amplitude + 1.0)
    spectrum = np.zeros(amplitude.shape,np.float32)
    cv2.normalize(amplitude,spectrum,0,1,cv2.NORM_MINMAX)
    return spectrum

#相位谱
def phaseSpectrum(fft2):
    rows,cols = fft2.shape[:2]
    phase = np.arctan2(fft2[:,:,1],fft2[:,:,0])
    spectrum = phase / math.pi * 180
    return spectrum

#快速傅里叶变换
def fft2Image(src):
    r,c = src.shape[:2]
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    fft2 = np.zeros((rPadded,cPadded,2),np.float32)
    fft2[:r,:c,0] = src
    cv2.dft(fft2,fft2,cv2.DFT_COMPLEX_OUTPUT)
    return fft2

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "usage:python spectrum.py imageFile"
    cv2.imshow("image",image)
    fft2 = fft2Image(image)
    amplitude = amplitudeSpectrum(fft2)
    ampSpetrum = graySpectrum(amplitude)
    #幅度谱的灰度级显示
    cv2.imshow("amlitudeSpectrum",ampSpetrum)
    phaseSpe = phaseSpectrum(fft2)
    #相位谱的灰度级显示
    cv2.imshow("phaseSpectrum",phaseSpe)
    #图像矩阵乘以(-1)^(r + c)
    rows,cols = image.shape
    fimg = np.copy(image)
    fimg = fimg.astype(np.float32)
    for r in xrange(rows):
        for c in xrange(cols):
            if (r + c) % 2:
                fimg[r][c] = -1 * image[r][c]
    #对中心化后的图像计算幅度谱和相位谱
    imgfft2 = fft2Image(fimg)
    amSpe = amplitudeSpectrum(imgfft2)
    graySpe = graySpectrum(amSpe)
    cv2.imshow("amSpe",graySpe)
    graySpe *= 255
    graySpe = graySpe.astype(np.uint8)
    cv2.imshow("centerAmp",graySpe)
    cv2.waitKey(0)
    cv2.destroyAllWindows();
