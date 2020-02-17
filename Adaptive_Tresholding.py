import cv2 
image = cv2.imread('photo-1472214103451-9374bd1c798e.jpg') 
#converting image to Gray scale 
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret,thresh_global = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
#here 11 is the pixel neighbourhood that is used to calculate the threshold value
thresh_mean = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thresh_gaussian = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('gray_imag',gray_image)
cv2.imshow('thresh_global',thresh_global)
cv2.imshow('thresh_mean',thresh_mean)
cv2.imshow('thresh_gaussian',thresh_gaussian)
cv2.waitKey(0)