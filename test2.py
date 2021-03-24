##
## Canny Edge Detection with object detection
##

import cv2
import numpy as np
import argparse
import glob
# from matplotlib import pyplot as plt

original = cv2.imread('SKR1.JPG')
gray = cv2.imread('SKR1.JPG',cv2.IMREAD_GRAYSCALE)

originalImg = cv2.resize(original, (300, 300))
grayImg = cv2.resize(gray, (300, 300))

# grayOut = cv2.cvtColor(originalImg, cv2.COLOR_BGR2GRAY)
ret, thresholdOut = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
blurOut = cv2.GaussianBlur(grayImg, (3, 3), 0)

## morfologi
# def morphologi(originalImg):
# frame = np.median(originalImg)
hsv = cv2.cvtColor(originalImg, cv2.COLOR_BGR2HSV)

lower = np.array([33,45,29])
upper = np.array([84,249,110])

mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(originalImg,originalImg, mask= mask)

kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(res,kernel,iterations = 1)
closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
bluring = cv2.GaussianBlur(closing,(5,5),0)

  # return closing


## auto canny
def auto_canny(originalImg, sigma=0.33):
  v = np.median(originalImg)

  lower = int(max(0, (1.0 - 0.33) * v))
  upper = int(min(255, (1.0 + 0.33) * v))
  edged = cv2.Canny(originalImg, lower, upper)

  return edged

wideOut = cv2.Canny(blurOut, 10, 200)
tightOut = cv2.Canny(blurOut, 225, 250)
autoOut = auto_canny(blurOut)

outputW = cv2.Canny(bluring, 10, 200)
outputT = cv2.Canny(bluring, 255, 250)
outputA = auto_canny(bluring)

cv2.imshow('image original',originalImg)
cv2.imshow('image gray',grayImg)
cv2.imshow('image binary',thresholdOut)
cv2.imshow('image blur ', blurOut)
cv2.imshow('image blur + closing', bluring)
cv2.imshow('image closing', closing)
cv2.imshow("Edges_1", np.hstack([wideOut, tightOut, autoOut]))
cv2.imshow("Edges_2", np.hstack([outputW, outputT, outputA]))
# cv2.imshow('image hsv', hsv)


cv2.waitKey(0)  
cv2.destroyAllWindows()
