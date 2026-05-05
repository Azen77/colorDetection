import os
import cv2
import numpy as np
from PIL import Image
from util import getlimits

yellow = [0,255,255]
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = getlimits(yellow)
    mask = cv2.inRange(hsvImage,lowerLimit,upperLimit)
    
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox() # coordinates x1,y1,x2,y2 of rectangle
    
    if bbox != None:
        frame = cv2.rectangle(frame,(bbox[0],bbox[1]),(bbox[2],bbox[3]),(0,255,0),3)
            
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()