# F55121006_Felisya Brigita Tania Wong_A

import cv2
from matplotlib import pyplot as plt

# Load image in BGR color space
img_bgr = cv2.imread('bloodCells.jpg')

# Convert BGR image to RGB color space
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Convert RGB image to HSV color space
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

# Display RGB image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('RGB Image')

# Display HSV image
plt.subplot(1, 2, 2)
plt.imshow(img_hsv)
plt.title('HSV Image')

plt.show()
