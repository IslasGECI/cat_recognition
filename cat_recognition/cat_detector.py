from cat_recognition.yolo_detections import (
    classify_from_path,
    Net_Yolo,
    is_there_a_cat,
    move_photo_with_detections,
)

class Cat_Detector:
    def __init__(self):
        self.net_yolo = Net_Yolo()

    def move_if_detection_is_positive(self, image_path, root_path):
        pass
