import os
import pickle

import cv2

from lab4.utils import get_image_paths, face_encodings

roor_dir = "dataset"
class_names = os.listdir(roor_dir)

image_paths = get_image_paths(roor_dir, class_names)
name_encodings_dict = {}

nb_current_image = 1

for image_path in image_paths:
    print(f"Image processed{nb_current_image}/{len(image_paths)}")
    image = cv2.imread(image_path)
    encodings = face_encodings(image)
    name = image_path.split(os.path.sep)[-2]
    e = name_encodings_dict.get(name, [])
    e.extend(encodings)
    name_encodings_dict[name] = e
    nb_current_image += 1

with open("encodings.pickle", "wb") as f:
    pickle.dump(name_encodings_dict, f)
