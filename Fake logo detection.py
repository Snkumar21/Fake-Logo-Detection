# Importing the module
import cv2

# Choose image
original = cv2.imread("Original Logo Path")
duplicate = cv2.imread("Detected Logo Path")

# Store the image shape into variable
ori_shape = original.shape[:2]
dup_shape = duplicate.shape[:2]

# TEST 1: Based on shape of image
if ori_shape == dup_shape:
    print("Image size is same")

    # Extract the difference of color element between two image
    difference = cv2.subtract(original, duplicate)
    b, g, r = cv2.split(difference)

    # TEST 2: Based on color of image
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The color is equal")
    else:
        print('The color of image is different')
        cv2.imshow('Difference', difference)

else:
    print("Image is different in size")

# Display image
cv2.imshow("Original",  original)
cv2.imshow("Duplicate", duplicate)
cv2.waitKey(0)
cv2.destroyAllWindows()
