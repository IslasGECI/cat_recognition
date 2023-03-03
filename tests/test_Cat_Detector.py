import pytest
import os
import cv2 as cv
from cat_recognition import (
    classify_from_path,
    Net_Yolo,
    is_there_a_cat,
    move_photo_with_detections,
    transform_image_to_blob,
    Cat_Detector,
)


class Test_Cat_Detector:
    def test_cat_detector_init(self):
        cat_detector = Cat_Detector()
        image_path = "/workdir/tests/data/resized/IMG_0586.jpg"
        assert not os.path.exists("/workdir/tests/data/cat_detected/IMG_0586.jpg")
        cat_detector.move_if_detection_is_positive(image_path, "/workdir/tests/data")
        assert os.path.exists("/workdir/tests/data/cat_detected/IMG_0586.jpg")
