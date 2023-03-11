import imutils
import numpy as np
import cv2

cv2.startWindowThread()

video = cv2.VideoCapture('IMG_0265.MOV')
face_cascade = cv2.CascadeClassifier(
    'C:\\Users\\User\\AppData\\Roaming\\Python\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

while True:
    ret, img = video.read()
    face_rects = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
    cv2.imshow("Lab2", img)

    if cv2.waitKey(1) & 0XFF == ord('g'):
        break

video.release()
cv2.destroyAllWindows()
