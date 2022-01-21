from imageai.Detection import ObjectDetection
import os

from os import listdir
from os.path import isfile, join

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
image_paths = [f"{files[:-4]}.jpg" for files in onlyfiles]
processed_image_paths = [f"{files[:-4]}_predicted.jpg" for files in onlyfiles]
input_images = [os.path.join(data_path, image_path) for image_path in image_paths]
paths_of_processed_image_as_negative = [
    os.path.join(negative_detections_path, processed_image_path)
    for processed_image_path in processed_image_paths
]
paths_of_processed_image_as_positive = [
    os.path.join(positive_detections_path, processed_image_path)
    for processed_image_path in processed_image_paths
]
custom_objects = detector.CustomObjects(cat=True)
inputs_and_paths = zip(
    input_images, paths_of_processed_image_as_negative, paths_of_processed_image_as_positive
)
for input_image, processed_as_positive, processed_as_positive in inputs_and_paths:
    detections = detector.detectCustomObjectsFromImage(
        minimum_percentage_probability=1,
        custom_objects=custom_objects,
        input_image=input_image,
        output_image_path=processed_as_positive,
    )
    name_objects = [individual_detection["name"] for individual_detection in detections]
    if "cat" in name_objects:
        os.replace(processed_as_positive, processed_as_positive)
