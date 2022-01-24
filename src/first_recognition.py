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


class Cat_Detector:
    def __init__(self):
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
        self.detector.loadModel()
        self.custom_objects = self.detector.CustomObjects(cat=True)

    def detect_cat(self, input_image, processed_as_positive):
        detections = self.detector.detectCustomObjectsFromImage(
            minimum_percentage_probability=1,
            custom_objects=self.custom_objects,
            input_image=input_image,
            output_image_path=processed_as_positive,
        )
        return detections


onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
image_paths = [f"{files[:-4]}.jpg" for files in onlyfiles]
input_images = [os.path.join(data_path, image_path) for image_path in image_paths]
processed_image_paths = [f"{files[:-4]}_predicted.jpg" for files in onlyfiles]
paths_of_processed_image_as_negative = [
    os.path.join(negative_detections_path, processed_image_path)
    for processed_image_path in processed_image_paths
]
paths_of_processed_image_as_positive = [
    os.path.join(positive_detections_path, processed_image_path)
    for processed_image_path in processed_image_paths
]
inputs_and_paths = zip(
    input_images, paths_of_processed_image_as_negative, paths_of_processed_image_as_positive
)
cat_detector = Cat_Detector()
for input_image, processed_as_negative, processed_as_positive in inputs_and_paths:
    detections = cat_detector.detect_cat(input_image, processed_as_negative)
    name_objects = [individual_detection["name"] for individual_detection in detections]
    if "cat" in name_objects:
        os.replace(processed_as_negative, processed_as_positive)
