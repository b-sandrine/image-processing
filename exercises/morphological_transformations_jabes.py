import cv2
import numpy as np
cap = cv2.VideoCapture(0)
def apply_distortion(img):
    rows, cols, ch = img.shape

    # Define the coordinates of the four corners of the mouth region
    mouth_corners = np.float32([[cols // 3, rows // 2], [2 * cols // 3, rows // 2], [cols // 3, 2 * rows // 3], [2 * cols // 3, 2 * rows // 3]])

    # Define the new coordinates of the four corners of the mouth region after stretching
    new_mouth_corners = np.float32([[cols // 3 - 20, rows // 2], [2 * cols // 3 + 20, rows // 2], [cols // 3, 2 * rows // 3], [2 * cols // 3, 2 * rows // 3]])

    # Create a matrix of transformation coefficients for the mouth-widening distortion
    coef = cv2.getPerspectiveTransform(mouth_corners, new_mouth_corners)

    # Apply the distortion to the input image
    distorted = cv2.warpPerspective(img, coef, (cols, rows))

    return distorted
while True:
    # Read a frame from the video capture object
    ret, frame = cap.read()

    # Apply the distortion to the frame
    distorted = apply_distortion(frame)

    # Display the original and distorted frames side-by-side
    both = cv2.hconcat([frame, distorted])
    cv2.imshow('Mouth-Widening Distortion', both)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()