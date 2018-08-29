# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:23:50 2018

@author: Administrator
"""

import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

def HTLine(image,stepTheta = 1,stepRho = 1):
    rows,cols = image.shape
    L = round(math.sqrt(pow(rows - 1,2.0) + pow(cols - 1,2.0))) + 1
    numtheta = int(180.0 / stepTheta)
    numRho = int(2 * L / stepRho + 1)
    accumulator = np.zeros((numRho,numtheta),np.int32)
    accuDict = {}
    for k1 in xrange(numRho):
        for k2 in xrange(numtheta):
            accuDict[(k1,k2)] = []
    for y in xrange(rows):
        for x in xrange(cols):
            if(image[y][x] == 255):
                for m in xrange(numtheta):
                    rho = x * math.cos(stepTheta * m / 180.0 * math.pi) + y * math.sin(
                            stepTheta * m / 180.0 * math.pi)
                    n = int(round(rho + L) / stepRho)
                    accumulator[n,m] += 1
                    accuDict[(n,m)].append((y,x))
    return accumulator,accuDict

if __name__ == "__main__":
    if len(sys.argv) > 1:
        I = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
    else:
        print "Usage:python prewitt.py imageFile"
    edge = cv2.Canny(I,50,200)
    cv2.imshow("edge",edge)
    accumulator,accuDict = HTLine(edge,1,1)
    rows,cols = accumulator.shape
    fig = plt.figure()
    ax = fig.gca(projection = "3d")
    X,Y = np.mgrid[0:rows:1,0:cols:1]
    surf = ax.plot_wireframe(X,Y,accumulator,cstride = 1,rstride = 1,color = "gray")
    ax.set_xlable(u"$\\rho$")
    ax.set_ylable(u"$\\theta$")
    ax.set_zlable("accumulator")
    ax.set_zlim3d(0,np.max(accumulator))
    grayAccu = accumulator / float(np.max(accumulator))
    grayAccu = grayAccu.astype(np.uint8)
    voteThresh = 60
    for r in xrange(rows):
        for c in xrange(cols):
            if accumulator[r][c] > voteThresh:
                points = accuDict[(r,c)]
                cv2.line(I,points[0],points[len(points) - 1],(255),2)
    cv2.imshow("accumulator",grayAccu)
    cv2.imshow("I",I)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
