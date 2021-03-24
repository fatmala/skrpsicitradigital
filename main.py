import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('SKR6.JPG')
#print(img.shape)
cv2.imshow('Gambar Asli', img)
cv2.waitKey(4)

img_scaled = cv2.resize(img, None, fx=0.1, fy=0.1)
#print(img_scaled.shape)
cv2.imshow('Gambar scaled', img_scaled)
cv2.waitKey(3)

img_gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gambar gray', img_gray)
cv2.waitKey(2)

#_ , img_threshold = cv2.threshold(img_gray, 125, 255, cv2.THRESH_BINARY)
#cv2.imshow('Gambar threshold', img_threshold)
#cv2.waitKey(2)

#img_canny = cv2.Canny(img_threshold, 100, 200)
#cv2.imshow('Gambar canny', img_canny)
#cv2.waitKey(1)

img_canny2 = cv2.Canny(img_gray, 200, 300)
cv2.imshow('Gambar Canny from Gray', img_canny2)
cv2.waitKey(1)

kernel = np.ones((5,5),np.uint8)

closing = cv2.morphologyEx(img_canny2, cv2.MORPH_CLOSE, kernel)
cv2.imshow('morfologi closing', closing)
cv2.waitKey(0)



#img6 = cv2.imread('SKR5.jpg',0)
#edges = cv2.Canny(img6,100,200)

plt.subplot(121),plt.imshow(img6,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

#plt.show()


