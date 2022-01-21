from imageai.Detection import ObjectDetection
import os

from os import listdir
from os.path import isfile, join

import cat_recognition as cr

execution_path = os.getcwd()
data_path = os.path.join(execution_path, "data/resized/")
results_path = os.path.join(execution_path, "data/processed/")
positive_detections_path = os.path.join(results_path, "cat_detected/")
negative_detections_path = os.path.join(results_path, "no_cat_detected/")

if not os.path.exists(positive_detections_path):
    os.mkdir(positive_detections_path)
if not os.path.exists(negative_detections_path):
    os.mkdir(negative_detections_path)


detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
detector.loadModel()


onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

custom_objects = detector.CustomObjects(cat=True)

for input_image, output_image_path in zip(input_images, output_image_paths):
    detections = detector.detectCustomObjectsFromImage(
        minimum_percentage_probability=1,
        custom_objects=custom_objects,
        input_image=input_image,
        output_image_path=output_image_path,
    )
    name_objects = [individual_detection["name"] for individual_detection in detections]
    if "cat" in name_objects:
        os.replace(output_image_path, os.path.join(positive_detections_path, processed_image_path))
