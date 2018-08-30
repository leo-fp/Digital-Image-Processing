# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018
谱残差显著性检测：
	(1)计算图像的快速傅里叶变换
	(2)计算幅度谱的灰度级graySpectrum
	(3)计算相位谱phaseSpectrum，然后根据相位谱计算对应的正弦谱和余弦谱
	(4)对第二步计算出的灰度级进行均值平滑
	(5)计算谱残差：graySpectrum与平滑结果的差
	(6)对谱残差进行幂指数运算
	(7)将第六步的结果作为新的幅度谱，使用原图的相位谱进行傅里叶逆变换
	(8)将第七步的结果取实部和虚部的平方和开放，然后高斯平滑，最后进行
     	   灰度级转换，即得到显著性

@author: Administrator
"""

import cv2
import numpy as np
import sys
import math

def amplitudeSpectrum(fft2):
    real2 = np.power(fft2[:,:,0],2.0)
    Imag2 = np.power(fft2[:,:,1],2.0)
    amplitude = np.sqrt(real2 + Imag2)
    return amplitude

def graySpectrum(amplitude):
    amplitude = np.log(amplitude + 1.0)
    spectrum = np.zeros(amplitude.shape,np.float32)
    cv2.normalize(amplitude,spectrum,0,1,cv2.NORM_MINMAX)
    return spectrum

def phaseSpectrum(fft2):
    rows,cols = fft2.shape[:2]
    phase = np.arctan2(fft2[:,:,1],fft2[:,:,0])
    spectrum = phase / math.pi * 180
    return spectrum

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
        print "usage:python fft2.py imageFile"
    cv2.imshow("image",image)
    fft2 = fft2Image(image)
    amplitude = amplitudeSpectrum(fft2)
    logAmplitude = graySpectrum(amplitude)
    phase = phaseSpectrum(fft2)
    cosSpectrum = np.cos(phase)
    sinSectrum = np.sin(phase)
    meanLogAmplitude = cv2.boxFilter(logAmplitude,cv2.CV_32FC1,(3,3))
    spectralResidual = logAmplitude - meanLogAmplitude
    expSR = np.exp(spectralResidual)
    real = expSR * cosSpectrum
    imaginary = expSR * sinSectrum
    com = np.zeros((real.shape[0],real.shape[1],2),np.float32)
    com[:,:,0] = real
    com[:,:,1] = imaginary
    ifft2 = np.zeros(com.shape,np.float32)
    cv2.dft(com,ifft2,cv2.DFT_COMPLEX_OUTPUT + cv2.DFT_INVERSE)
    saliencymap = np.power(ifft2[:,:,0],2) + np.power(ifft2[:,:,1],2)
    saliencymap = cv2.GaussianBlur(saliencymap,(31,31),2.5)
    saliencymap = saliencymap / np.max(saliencymap)
    saliencymap = np.power(saliencymap,0.5)
    saliencymap = np.round(saliencymap * 255)
    saliencymap = saliencymap.astype(np.uint8)
    cv2.imshow("saliencymap",saliencymap)
    cv2.waitKey(0)
    cv2.destroyAllWindows();
