import imutils
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\User\\AppData\\Roaming\\Python\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('C:\\Users\\User\\AppData\\Roaming\\Python\\Python39\\site-packages\\cv2\\data\\haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\User\\AppData\\Roaming\\Python\\Python39\\site-packages\\cv2\\data\\haarcascade_eye.xml')
#img = cv2.imread("Tony-Stark-home-Avengers-Endgame.jpg")
img = cv2.imread("people.jpg")
face_rects = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
print("Found in img faces: ", len(face_rects))
for(x, y, w, h) in face_rects:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)
    face = img[y:y+h, x:x+w]
    smile = smile_cascade.detectMultiScale(face)
    eye = eye_cascade.detectMultiScale(face)
    for(smile_x, smile_y, smile_w, smile_h) in smile:
        cv2.rectangle(face, (smile_x, smile_y), (smile_x+smile_w, smile_y+smile_h), (0, 255, 0), 2)
    for (eye_x, eye_y, eye_w, eye_h) in eye:
        cv2.rectangle(face, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (0, 0, 255), 2)
cv2.imshow("Lab2", img)
cv2.waitKey(0)