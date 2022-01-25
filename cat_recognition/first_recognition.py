from imageai.Detection import ObjectDetection
import os
from os import listdir
from os.path import isfile, join


class Paths:
    PROCESSED_IMAGE_AS_NEGATIVE = "processed_image_as_negative"
    PROCESSED_IMAGE_AS_POSITIVE = "processed_image_as_positive"


def move_if_detection_is_positive(detections, processed_as_negative, processed_as_positive):
    name_objects = [individual_detection["name"] for individual_detection in detections]
    if "cat" in name_objects:
        os.replace(processed_as_negative, processed_as_positive)


class Cat_Detector:
    def __init__(self):
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()

    def set_model_path(self, execution_path):
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


class Paths_Management:
    def __init__(self, execution_path):
        self.data_path = os.path.join(execution_path, "data/resized/")
        self.results_path = os.path.join(execution_path, "data/processed/")
        self.positive_detections_path = os.path.join(self.results_path, "cat_detected/")
        self.negative_detections_path = os.path.join(self.results_path, "no_cat_detected/")
        self.onlyfiles = [f for f in listdir(self.data_path) if isfile(join(self.data_path, f))]

    def setup_directory_processed(self):
        if not os.path.exists(self.positive_detections_path):
            os.mkdir(self.positive_detections_path)
        if not os.path.exists(self.negative_detections_path):
            os.mkdir(self.negative_detections_path)

    def get_input_images_paths(self):
        image_paths = [f"{files[:-4]}.jpg" for files in self.onlyfiles]
        self.input_images = [os.path.join(self.data_path, image_path) for image_path in image_paths]

    def get_processed_images_paths(self):
        processed_image_paths = [f"{files[:-4]}_predicted.jpg" for files in self.onlyfiles]
        paths_of_processed_image_as_negative = [
            os.path.join(self.negative_detections_path, processed_image_path)
            for processed_image_path in processed_image_paths
        ]
        paths_of_processed_image_as_positive = [
            os.path.join(self.positive_detections_path, processed_image_path)
            for processed_image_path in processed_image_paths
        ]
        self.paths = {
            Paths.PROCESSED_IMAGE_AS_NEGATIVE: paths_of_processed_image_as_negative,
            Paths.PROCESSED_IMAGE_AS_POSITIVE: paths_of_processed_image_as_positive,
        }

    def get_input_output_paths(self):
        self.get_input_images_paths()
        self.get_processed_images_paths()
        inputs_and_paths = zip(
            self.input_images,
            self.paths[Paths.PROCESSED_IMAGE_AS_NEGATIVE],
            self.paths[Paths.PROCESSED_IMAGE_AS_POSITIVE],
        )
        return inputs_and_paths
