import imutils
import numpy as np
import cv2
img = cv2.imread ('foto.jpg')
#cv2.imshow("My img", img)
output = img.copy()
#cv2.rectangle(output, (270, 50), (890, 560), (0, 120, 255), 2)
#cv2 . circle (output, (600, 300), 275, (100, 140, 255), 2)
#resized = imutils.resize(img, height=300)
#rotated = imutils.rotate(img, -45)
#blurred = cv2.GaussianBlur (img, (11, 11), 0)
#cv2.imshow ("Blurred", blurred)

#font2 =cv2 . FONT_HERSHEY_SCRIPT_COMPLEX
#cv2 . putText (output, 'First time',(10, 500), font2, 4,(255, 255, 255),2 ,cv2.LINE_4)
cv2.line(img,(300, 0),(300, 800),(0,100, 255),5)

cv2.imshow ("Rectangle", img)
cv2.waitKey()
cv2.destroyAllWindows()

