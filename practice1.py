import cv2

img = cv2.imread("/home/sandrine/Documents/s6_resources/embedded-systems/python-practice/imageProcessingByInstructor/lena.jpg")
img_gray = cv2.cvtCOLOR(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)
cv2.imshow("Image grayed", img_gray)
cv2.waitKey(0)