import cv2
import numpy as np

input = cv2.imread("./images/input.jpg")

cv2.imshow("Hello World", input)

a = input.shape
print('Shape of the image', a)

print("height of the image", int(input.shape[0]), "pixels")

cv2.waitKey()

cv2.destroyAllWindows()