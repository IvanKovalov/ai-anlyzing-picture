import cv2
import numpy

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

video = cv2.VideoCapture('People.mkv')

while True:
    ret, img = video.read()
    img = cv2.resize(img, (800, 500))
    gary_filter = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    boxes, weights = hog.detectMultiScale(gary_filter)
    boxes = numpy.array([[x, y, x+w, y+h] for (x, y, w, h) in boxes])
    for (xa, ya, xw, yh) in boxes:
       cv2.rectangle(gary_filter, (xa, ya), (xw, yh), (0, 255, 0), 2)

    cv2.imshow("PeopleDetector", gary_filter)
    if cv2.waitKey(1) & 0XFF == ord('g'):
       break

video.release()
cv2.destroyAllWindows()


#img = cv2.imread('dark.jpg')
#img = cv2.resize(img, (800, 500))
#gary_filter = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#boxes, weights = hog.detectMultiScale(gary_filter)
#boxes = numpy.array([[x, y, x+w, y+h] for (x, y, w, h) in boxes])
#for (xa, ya, xw, yh) in boxes:
#    cv2.rectangle(gary_filter, (xa, ya), (xw, yh), (0, 255, 0), 2)

#cv2.imshow("PeopleDetector", gary_filter)
#cv2.waitKey(0)