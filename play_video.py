import numpy as np
import cv2
import time
cap = cv2.VideoCapture('/home/pankaj/Documents/stocks/video.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(1)
cap.release()
cv2.destroyAllWindows()
