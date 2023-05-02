import numpy as np
import cv2
image = cv2.imread('/home/sandrine/Documents/s6_resources/embedded-systems/python-practice/imageProcessingByInstructor/lena_resized.jpg')
y=250
x=220
h=200
w=200
cropped = image[y:y+h, x:x+w]

# Save cropped image
cv2.imwrite("/home/sandrine/Documents/s6_resources/embedded-systems/python-practice/imageProcessingByInstructor/lena_cropped.jpg", cropped)

cv2.imshow('Lena Cropped', cropped)
cv2.waitKey(0)