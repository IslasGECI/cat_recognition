import os

from cat_recognition import Cat_Detector, Paths_Management, move_if_detection_is_positive


execution_path = os.getcwd()
paths_management = Paths_Management(execution_path)
paths_management.setup_directory_processed()
inputs_and_paths = paths_management.get_input_output_paths()
cat_detector = Cat_Detector()
cat_detector.set_model_path(execution_path)
for input_image, processed_as_negative, processed_as_positive in inputs_and_paths:
    detections = cat_detector.detect_cat(input_image, processed_as_negative)
    move_if_detection_is_positive(detections, processed_as_negative, processed_as_positive)
