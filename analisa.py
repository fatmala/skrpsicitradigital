import cv2
import numpy as np
import csv
from matplotlib import pyplot as plt
from numpy import genfromtxt
import imutils



## ekstraksi fitur warna
# #testing
# img = cv2.imread('a1.JPG', -1)
# # cv2.imshow('GoldenGate',img)
# query = cv2.calcHist([img],[1],None,[151],[0,151])	

# #training
# myArray =[]
# # print(len(myArray))
# for i in range(14,15):
# 		img = cv2.imread('a'+str(i)+'.JPG', -1)
# 		# cv2.imshow('GoldenGate',img)
# 		histr = cv2.calcHist([img],[1],None,[151],[0,151])	
# 		myArray.append(histr)
# 		print(histr)
# 		# myArray = histr
# 		# myArray=np.array([histr])  #func used to convert [1,2,3] list into an array
		
# print(len(myArray[0]))

# for x in range(len(myArray)):
# 	for y in range(len(myArray[0])):
# 		print(str(myArray[x][y])+ "\t")


# for x in myArray:
# 	print(str(myArray)+'\t')

# with open('warna_testing.csv', 'w') as f:
#     for d in myArray:
#         f.write(str(d))
#         # f.write("\n")


## ekstraksi fitur bentuk

# #testing
# query = []
# img = cv2.imread('17.JPG', -1)
# #print(img.shape)
# # cv2.imshow('Gambar Asli', img)
# # cv2.waitKey(4)
# img_scaled = cv2.resize(img, None, fx=0.1, fy=0.1)
# # #print(img_scaled.shape)
# # cv2.imshow('Gambar scaled', img_scaled)
# # cv2.waitKey(3)
# # img_scaled2 = img_scaled.copy()	# img_scaled3 = img_scaled.copy()
# img_gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)
# # cv2.imshow('Gambar gray', img_gray)
# #cv2.waitKey(2)
# #_ , img_threshold = cv2.threshold(img_gray, 125, 255, cv2.THRESH_BINARY)
# #cv2.imshow('Gambar threshold', img_threshold)
# #cv2.waitKey(2)
# #img_canny = cv2.Canny(img_threshold, 100, 200)
# #cv2.imshow('Gambar canny', img_canny)
# #cv2.waitKey(1)

# img_canny2 = cv2.Canny(img_gray, 200, 300)
# # cv2.imshow('Gambar Canny from Gray', img_canny2)
# # cv2.waitKey(1)

# kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(img_canny2, cv2.MORPH_CLOSE, kernel)

# contours, hierarchy = cv2.findContours(closing,  
# 	    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

# area=0
# equi_diameter=0
# for x in range(len(contours)):
# 	area += cv2.contourArea(contours[x]) 
# 	equi_diameter = np.sqrt(4*area/np.pi)  
# # print("Number of Contours found = " + str(len(contours))) 
# query.append(area)
# query.append(equi_diameter)
# # print(str(area)+"\t") 
# # print(str(equi_diameter)+"\t") 
  
# # Draw all contours 
# # -1 signifies drawing all contours 
# # cv2.drawContours(img_scaled, contours, -1, (0, 255, 0), 3) 
  
# # cv2.imshow('Contours', img_scaled) 
# # cv2.waitKey(1) 


# perimeter = 0
# for x in range(len(contours)):
# 	peri = cv2.arcLength(contours[x], True)
# 	approx = cv2.approxPolyDP(contours[x], 0.02 * peri, True)
# 	perimeter += peri 

# # cv2.drawContours(img_scaled, [approx], -1, (255, 0, 0), 2)
# # print(str(perimeter)+"\n") 
# query.append(perimeter)	
# # cv2.imshow('perimeter', img_scaled) 
# # cv2.waitKey(0) 
# # cv2.destroyAllWindows() 

# myArray =[]
# for i in range(1,15):
# 	Array = []
# 	img = cv2.imread('a'+str(i)+'.JPG')
# 	img_scaled = cv2.resize(img, None, fx=0.1, fy=0.1)
# 	img_gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)
# 	img_canny2 = cv2.Canny(img_gray, 200, 300)
# 	kernel = np.ones((5,5),np.uint8)
# 	closing = cv2.morphologyEx(img_canny2, cv2.MORPH_CLOSE, kernel)
# 	contours, hierarchy = cv2.findContours(closing,  
# 	    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
# 	area=0
# 	equi_diameter=0
# 	for x in range(len(contours)):
# 		area += cv2.contourArea(contours[x]) 
# 		equi_diameter = np.sqrt(4*area/np.pi)  
# 	Array.append(area)
# 	Array.append(equi_diameter) 
# 	perimeter = 0
# 	for x in range(len(contours)):
# 		peri = cv2.arcLength(contours[x], True)
# 		approx = cv2.approxPolyDP(contours[x], 0.02 * peri, True)
# 		perimeter += peri 
# 	Array.append(perimeter)
# 	myArray.append(Array)
# 	print(str(area)+'\t'+ str(equi_diameter)+'\t'+ str(perimeter)) 
# print(myArray)
# cv2.imshow('perimeter', img_scaled2) 
# cv2.waitKey(1) 

# with open('shape.csv', 'w') as f:
#     for d in myArray:
#         f.write(str(d))
#         f.write("\n")


# hulls = 0
# for x in range(len(contours)):
# 	hull = cv2.convexHull(contours[x])
# 	cv2.drawContours(img_scaled3, contours = [hull], 
#                             contourIdx = 0, 
#                             color = (255, 0, 0), thickness = 2)
# 	hulls += hull
# print("Hull = " + str(hulls)) 
# cv2.imshow('Hull', img_scaled3) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows()

# print("1st Contour Area : ", cv2.contourArea(contours[0])) # 37544.5
# print("2nd Contour Area : ", cv2.contourArea(contours[1])) # 75.0
# print("3rd Contour Area : ", cv2.contourArea(contours[2])) # 54.0

query = genfromtxt('all_testing.csv', delimiter=',')
myArray = genfromtxt('all_training.csv', delimiter=',')

from sklearn import preprocessing

quer_a=np.reshape(myArray[116], (1, -1))
query_normalized = preprocessing.normalize(quer_a, norm='l1')

for x in range(len(query_normalized)):
	for y in range(len(query_normalized[x])):
		print(query_normalized[x][y])




# #euclidean_distance
# for x in range(len(myArray)):
# 	sume = 0
# 	for y in range(len(myArray[0])):
# 		sume += (query[9][y]-myArray[x][y])**2
# 	euclidean_distance = np.sqrt(sume)
# 	print(euclidean_distance)	
# 		# print(myArray[x][y], end = '  ')
# 	# print()