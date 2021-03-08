import cv2
import numpy as np

#create video reader
video = cv2.VideoCapture(0)

for i in range(0, 60):
    ret, background = video.read()

    background = cv2.flip(background, 1)

while True:
    ret, img = video.read()

    img = cv2.flip(img, 1)

    #convert img from brg to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #create fillter for red
    lower = np.array([0, 255, 34])
    upper = np.array([185, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    #replace the red color with the background in same index
    img[np.where(mask == 255)] = background[np.where(mask == 255)]

    cv2.imshow("Display", img)

    #for debug only
    #cv2.imshow("Threshhold", mask)

    #read quit key
    quitKey = cv2.waitKey(1)
    
    if quitKey == ord('q'):
        break

#quit program
video.release()
cv2.destroyAllWindows()