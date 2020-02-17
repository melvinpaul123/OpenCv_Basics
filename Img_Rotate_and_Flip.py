import cv2

img = cv2.imread('photo-1472214103451-9374bd1c798e.jpg')


img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)

img_flip_ud = cv2.flip(img, 0)

img_flip_lr = cv2.flip(img, 1)

img_flip_ud_lr = cv2.flip(img, -1)
 
cv2.imshow('img',img)
cv2.imshow('img_rotate_90_clockwise',img_rotate_90_clockwise)
cv2.imshow('img_rotate_90_counterclockwise',img_rotate_90_counterclockwise)
cv2.imshow('img_rotate_180',img_rotate_180)
cv2.imshow('img_flip_ud',img_flip_ud)
cv2.imshow('img_flip_lr',img_flip_lr)
cv2.imshow('img_flip_ud_lr',img_flip_ud_lr)
cv2.waitKey(0)