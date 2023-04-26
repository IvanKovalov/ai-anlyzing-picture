import cv2

from utils import get_image_paths, face_encodings

#class_names = ['Arnold_Schwarzenegger']
#image_paths = get_image_paths("dataset, class_names")

#print(image_paths)
image = cv2.imread("dataset/Arnold_Schwarzenegger/Arnold_Schwarzenegger_0001.jpg")
print(face_encodings(image))
print(face_encodings(image)[0].shape)
