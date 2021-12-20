import cv2
import sys 

img = cv2.imread('filename.jpg')
if img is None:
    sys.exit('img is none')

cv2.imshow('Window','filenamw.jpg')
k = cv2.waitKey(0)


