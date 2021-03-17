import cv2
import numpy as np
import pyttsx3
voice = pyttsx3.init()

cap = cv2.VideoCapture(0)

y_lower = np.array([22, 93, 0])
y_upper = np.array([45, 255, 255])
prev_y = 0
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,y_lower,y_upper)
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
            voice.say("Yellow detected! Yellow detected!")
            voice.runAndWait()
            x,y,w,h = cv2.boundingRect(i)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
            if y < prev_y:
                voice.say('You are moving the item down. Hold it still please.')
                voice.runAndWait()
            prev_y = y

    cv2.imshow('camera',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(10) == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()
