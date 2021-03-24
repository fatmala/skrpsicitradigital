import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('SKR10.JPG')
img2 = cv2.resize(img , (550,350))


print(img.shape) # (152, 203, 3) = (tinggi, lebar, channel gambar)
print(img[0][0][0]) # mengakses pixel warna BIRU di titik paling kiri atas
print(img[0][0][1]) # mengakses pixel warna HIJAU di titik paling kiri atas
print(img[0][0][2])

img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
print(cv2.mean(img_gray))



cv2.imshow('gambar abu',img_gray)
plt.hist(img_gray.ravel(),256,[0,256]); plt.show()