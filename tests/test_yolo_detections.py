import os
import cat_recognition as cr
from cat_recognition.yolo_detections import classify_from_path, Net_Yolo, is_there_a_cat


class Test_Cat_Detector:
    def test_init(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/data/resized/IMG_0586.jpg"
        self.outs = classify_from_path(image_path, net_yolo)

    def test_there_is_a_cat(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/data/resized/IMG_0586.jpg"
        self.outs = classify_from_path(image_path, net_yolo)
        assert is_there_a_cat(self.outs)

    def test_there_is_not_a_cat(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/data/resized/IMG_0588.jpg"
        self.outs = classify_from_path(image_path, net_yolo)
        assert is_there_a_cat(self.outs)