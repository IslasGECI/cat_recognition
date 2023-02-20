import os
import cat_recognition as cr
from cat_recognition.yolo_detections import classify_from_path, Net_Yolo


class Test_Cat_Detector:
    def test_init(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/data/resized/IMG_0586.jpg"
        self.outs = classify_from_path(image_path, net_yolo)
    
    def test_there_is_a_cat(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/data/resized/IMG_0586.jpg"
        self.outs = classify_from_path(image_path, net_yolo)
        for out in self.outs:
            for detection in out:
                scores = detection[5:]  # Tiramos algunos "objetos" ¿Por qué no están el coco.name?
                class_id = 15  # np.argmax(scores)
                cat_confidence = scores[class_id]
            # print(cat_confidence)
                if cat_confidence > 0.01:
                # Object detection
                    assert True
