#import the required libraries 
import cv2 
image = cv2.imread('photo-1472214103451-9374bd1c798e.jpg') 
#converting image to Gray scale 
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#converting image to HSV format
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('0riginal',image)
imagergb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow('gray_imag',gray_image)
cv2.imshow('hsv_image',hsv_image)
cv2.imshow('imagergb',imagergb)
cv2.waitKey(0)