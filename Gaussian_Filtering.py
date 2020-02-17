import numpy as np 
import cv2 
image = cv2.imread('photo-1472214103451-9374bd1c798e.jpg') 
cv2.imshow('image',image)
#using the averaging kernel for image smoothening 
averaging_kernel = np.ones((3,3),np.float32)/9 
filtered_image1 = cv2.filter2D(image,-1,averaging_kernel) 
cv2.imshow('filtered_image1',filtered_image1)

#get a one dimensional Gaussian Kernel 
gaussian_kernel_x = cv2.getGaussianKernel(5,1) 
gaussian_kernel_y = cv2.getGaussianKernel(5,1) 
#converting to two dimensional kernel using matrix multiplication 
gaussian_kernel = gaussian_kernel_x * gaussian_kernel_y.T 
#you can also use cv2.GaussianBLurring(image,(shape of kernel),standard deviation) instead of cv2.filter2D 
filtered_image2 = cv2.filter2D(image,-1,gaussian_kernel) 
cv2.imshow('filtered_image2',filtered_image2)
cv2.waitKey(0)
#Gaussian filtering is also used for image blurring that gives different weights to the 
#neighbouring pixels based on their distance from the pixel under consideration.
#For image filtering, we use kernels. Kernels are matrices of numbers of different shapes like 
#3 x 3, 5 x 5, etc. A kernel is used to calculate the dot product with a part of the image. 
#When calculating the new value of a pixel, the kernel center is overlapped with the pixel. 
#The neighbouring pixel values are multiplied with the corresponding values in the kernel. 
#The calculated value is assigned to the pixel coinciding with the center of the kernel.
#We can see that the edges of the original image are suppressed. 
#The Gaussian kernel with different values of sigma is used extensively to calculate the Difference of Gaussian for our image. 
#This is an important step in the feature extraction process because it reduces the noise present in the image.