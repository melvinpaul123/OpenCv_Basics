import cv2 
import numpy as np
image = cv2.imread('1_xRRF-PLCcIITBiXzTScwGQ.png') 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
image[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',image)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

#high accuracy   
#import cv2 
#import numpy as np
#image = cv2.imread('1_xRRF-PLCcIITBiXzTScwGQ.png') 
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#gray = np.float32(gray)    
#dst = cv2.cornerHarris(gray,2,3,0.04)
#dst = cv2.dilate(dst,None)
#ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
#dst = np.uint8(dst)

# find centroids
#ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
#criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
#corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
#res = np.hstack((centroids,corners))
#res = np.int0(res)
#image[res[:,1],res[:,0]]=[0,0,255]
#image[res[:,3],res[:,2]] = [0,255,0]
#cv2.imshow('dst',image)
#if cv2.waitKey(0) & 0xff == 27:
 #   cv2.destroyAllWindows()