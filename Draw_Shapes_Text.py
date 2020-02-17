import cv2
import numpy as np
# Create a black image
img = np.zeros((512,512,3),np.uint8)
# 0 255
#print(img)
#img[:] = 255 ,0,0
# Draw a diagonal green line with thickness of 2 px
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)

cv2.rectangle(img,(350,100),(450,200),(0,0,255),cv2.FILLED)
cv2.circle(img,(150,400),50,(255,0,0),3)
cv2.putText(img,"Draw Shapes ",(75,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
#One argument is the center location (x,y). Next argument is axes lengths (major axis length, minor axis length). 
#angle is the angle of rotation of ellipse in anti-clockwise direction. startAngle and endAngle denotes the starting and
# ending of ellipse arc measured in clockwise direction from major axis. i.e. giving values 0 and 360 gives the full ellipse. 
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2
#where ROWS are number of vertices and it should be of type int32. Here we draw a small polygon of with four vertices in yellow color.
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

#cv2.polylines() can be used to draw multiple lines. Just create a list of all the lines you want to draw 
#and pass it to the function. All lines will be drawn individually. It is more better and faster way to draw a 
#group of lines than calling cv2.line() for each line.

cv2.imshow("Image", img)

cv2.waitKey(0)
#lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA 
#gives anti-aliased line which looks great for curves.