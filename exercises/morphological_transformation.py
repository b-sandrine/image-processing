import cv2
import numpy as np

# Load image
img = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Create a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Apply erosion operation
erosion = cv2.erode(img, kernel, iterations=1)

# Apply dilation operation
dilation = cv2.dilate(img, kernel, iterations=1)

# Display the original image and the result
cv2.imshow('Original Image', img)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
