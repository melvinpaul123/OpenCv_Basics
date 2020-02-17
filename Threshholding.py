#import the required libraries 
import cv2 
import numpy as np
image = cv2.imread('photo-1472214103451-9374bd1c798e.jpg') 

#converting image to Gray scale 
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret,thresh_binary = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
ret,thresh_binary_inv = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh_trunc = cv2.threshold(gray_image,127,255,cv2.THRESH_TRUNC)
ret,thresh_tozero = cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO)
ret,thresh_tozero_inv = cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO_INV)
gray_image = cv2.resize(gray_image, (0, 0), None, 0.5, 0.5)
thresh_binary = cv2.resize(thresh_binary, (0, 0), None, 0.5, 0.5)
thresh_binary_inv = cv2.resize(thresh_binary_inv, (0, 0), None, 0.5, 0.5)
thresh_trunc = cv2.resize(thresh_trunc, (0, 0), None, 0.5, 0.5)
thresh_tozero = cv2.resize(thresh_tozero, (0, 0), None, 0.5, 0.5)
thresh_tozero_inv = cv2.resize(thresh_tozero_inv, (0, 0), None, 0.5, 0.5)
#cv2.imshow('gray_image',gray_image)
#cv2.imshow('thresh_binary',thresh_binary)
#cv2.imshow('thresh_binary_inv',thresh_binary_inv)
#cv2.imshow('thresh_trunc',thresh_trunc)
#cv2.imshow('thresh_tozero',thresh_tozero)
#cv2.imshow('thresh_tozero_inv',thresh_tozero_inv)
hor1= np.hstack((gray_image, thresh_binary,thresh_binary_inv))
hor2= np.hstack((thresh_trunc, thresh_tozero,thresh_tozero_inv ))
ver = np.vstack((hor1, hor2))
cv2.imshow('thresholding', ver)
cv2.waitKey(0)