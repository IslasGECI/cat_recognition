import pytest
import os
import cv2 as cv
from cat_recognition.yolo_detections import (
    classify_from_path,
    Net_Yolo,
    is_there_a_cat,
    move_photo_with_detections,
    transform_image_to_blob,
)


class Test_Cat_Detector:
    def test_init(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/tests/data/resized/image3.jpg"
        self.outs = classify_from_path(image_path, net_yolo)

    def test_there_is_a_cat(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/tests/data/resized/IMG_0586.jpg"
        self.outs = classify_from_path(image_path, net_yolo)
        assert is_there_a_cat(self.outs)

    def test_there_is_not_a_cat(self):
        net_yolo = Net_Yolo()
        image_path = "/workdir/tests/data/resized/IMG_0588.jpg"
        self.outs = classify_from_path(image_path, net_yolo)
        assert not is_there_a_cat(self.outs)


def test_move_photo_with_detections():
    f = open("/workdir/tests/data/resized/demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    assert not os.path.exists("/workdir/tests/data/cat_detected/demofile2.txt")
    move_photo_with_detections("demofile2.txt", "/workdir/tests/data")
    assert os.path.exists("/workdir/tests/data/cat_detected/demofile2.txt")
    os.remove("/workdir/tests/data/cat_detected/demofile2.txt")


def test_is_there_a_cat():
    outs = [
        [
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0.16,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]
        ]
    ]
    assert not is_there_a_cat(outs, 0.16)
    assert is_there_a_cat(outs, 0.15)


def test_transform_image_to_blob():
    image_path = "/workdir/tests/data/image3.jpg"
    img = cv.imread(image_path)
    blob = transform_image_to_blob(img)
    assert blob[0][0][0][0] == pytest.approx(0.55272, 0.01)
    assert blob[0][1][0][0] == pytest.approx(0.48216, 0.01)
    assert blob[0][2][0][0] == pytest.approx(0.40376, 0.01)
