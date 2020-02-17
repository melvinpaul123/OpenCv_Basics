import cv2 
image = cv2.imread('1_xRRF-PLCcIITBiXzTScwGQ.png') 
cv2.imshow('image',image)
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #cv2.CHAIN_APPROX_NONE
with_contours = cv2.drawContours(image,contours,-1,(0,255,0),2) 
cv2.imshow('with_contours',with_contours)
cv2.waitKey(0)