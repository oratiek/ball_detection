import cv2
import numpy as np

class Detector:
    def __init__(self, maxRadius, minRadius):
        self.maxRadius = maxRadius
        self.minRadius = minRadius
        self.MODE = 0
        self.COLOR = (255,255,0)

    def get_circle(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 5)
        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT,
                                dp=1, minDist=10, param1=30, param2=30,
                                minRadius=self.minRadius,maxRadius=self.maxRadius)
        try:
            circles = np.uint16(np.around(circles))
            print(circles)
            return circles[0]
        except TypeError:
            print("not found")
            return []

    def set_mode(self, mode):
        """
        (This method is for self.demo())
        Specify mode with index number
        0 : just circle
        1 : draw dot 
        2 : draw dot (last 10 dots)
        """
        self.MODE = mode
    
    def set_color(self, color):
        """
        get (R,G,B) data as input
        if input is not color data print "color set failed, set to default color"
        """
        change_status = True
        # data needs to be tuple
        if type(color) == tuple and len(color) == 3:
            self.COLOR = color
        elif type(color) != tuple:
            print("color data needs to be tuple but got {}".format(type(color).__name__))
            change_status = False
        elif len(color) != 3:
            print("color data needs 3 data which are (R,G,B)")
            change_status = False

        if not change_status:
            print("color set failed, set to default color")
            

    def demo(self):
        cap = cv2.VideoCapture(0)
        if self.MODE == 0:
            while True:
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
                frame = cv2.flip(frame, 1)
                ball = self.get_circle(frame)
                if len(ball) != 0:
                    for x,y,r in ball:
                        frame = cv2.circle(frame, (x,y), r, self.COLOR, 2)
                cv2.imshow("",frame)
                if cv2.waitKey(1) == ord("q"):
                    break
        elif self.MODE == 1:
            while True:
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
                frame = cv2.flip(frame, 1)
                ball = self.get_circle(frame)
                if len(ball) != 0:
                    for x,y,r in ball:
                        cv2.circle(frame, (x,y), r, self.COLOR, 2)
                        cv2.circle(frame, (x,y), 1, self.COLOR, 2)
                cv2.imshow("", frame)
                if cv2.waitKey(1) == ord("q"):
                    break

        elif self.MODE == 2:
            dots = []
            while True:
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
                frame = cv2.flip(frame, 1)
                ball = self.get_circle(frame)
                if len(ball) != 0:
                    for x,y,r in ball:
                        if len(dots) == 10:
                            dots.pop(0)
                        dots.append([x,y])
                        cv2.circle(frame, (x,y), r, self.COLOR, 2)
                for dot_data in dots:
                    x = dot_data[0]
                    y = dot_data[1]
                    cv2.circle(frame, (x,y), 1, self.COLOR, 2)
                cv2.imshow("", frame)
                if cv2.waitKey(1) == ord("q"):
                    break
