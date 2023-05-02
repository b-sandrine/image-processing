import cv2

img = cv2.imread("/home/sandrine/Documents/s6_resources/embedded-systems/python-practice/imageProcessingByInstructor/lena.jpg")
img_blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("Original", img)
cv2.imshow("Image blur", img_blur)
cv2.waitKey(0)