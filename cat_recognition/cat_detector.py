from cat_recognition.yolo_detections import (
    classify_from_path,
    Net_Yolo,
    is_there_a_mammals,
    move_photo_with_detections,
)


class Cat_Detector:
    def __init__(self, cut_prob=0.01):
        self.net_yolo = Net_Yolo()
        self.cut_prob: float = cut_prob

    def move_if_detection_is_positive(self, image_path, root_path):
        outs = classify_from_path(image_path, self.net_yolo)
        if is_there_a_mammals(outs, self.cut_prob):
            name_image = image_path.split("/")[-1]
            move_photo_with_detections(name_image, root_path)
            return name_image
