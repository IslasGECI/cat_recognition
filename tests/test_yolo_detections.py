import os
import shutil
from cat_recognition.yolo_detections import classify_from_path, Net_Yolo, is_there_a_cat, move_photo_with_detections


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
    assert not os.path.exists("/workdir/tests/data/detected_cat/demofile2.txt")
    os.remove("/workdir/tests/data/resized/demofile2.txt")
    move_photo_with_detections()
    assert os.path.exists("/workdir/tests/data/detected_cat/demofile2.txt")
    pass