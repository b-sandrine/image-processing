import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('image.jpg', 0)

# Apply Gaussian blur to reduce noise
img_blur = cv2.GaussianBlur(img, (3, 3), 0)

# Use the Canny edge detection algorithm
edges = cv2.Canny(img_blur, 100, 200)

# Display the original image and the edges
cv2.imshow('Original Image', img)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
