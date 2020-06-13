import cv2
import numpy as np
from detector import Detector

detector = Detector(30,50)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    ball = detector.get_circle(frame)
    for x,y,r in ball:
        cv2.circle(frame, (x,y), r, (255,255,0), 2)
    cv2.imshow("",frame)
    if cv2.waitKey(1) == ord("q"):
        break
