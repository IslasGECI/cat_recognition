import os
import cat_recognition as cr
from cat_recognition.yolo_detections import classify_from_path, Net_Yolo


class Test_Cat_Detector:
    def test_init(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/data/resized/IMG_0586.jpg"
        self.outs = classify_from_path(image_path, net_yolo)


