#use to create filter for invisible coalk

import cv2
import numpy as np
import sys

b = int(sys.argv[1])
g = int(sys.argv[2])
r = int(sys.argv[3])

color = np.uint8([[[b,g,r ]]])

hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)

print(hsv)