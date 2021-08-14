import numpy as np
import cv2 as cv
img = cv.imread('d:/blank_ct.png')
average_image = cv.blur(img,(3,3))
cv.imshow('blur', average_image)
cv.imshow('orig', img)
cv.waitKey()