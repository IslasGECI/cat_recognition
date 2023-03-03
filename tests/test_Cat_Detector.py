import os
import shutil
from cat_recognition import Cat_Detector


class Test_Cat_Detector:
    def test_cat_detector_init(self):
        shutil.copyfile(
            "/workdir/tests/data/resized/IMG_0586.jpg", "/workdir/tests/data/resized/IMG_0586-2.jpg"
        )
        output_path = "/workdir/tests/data/cat_detected/IMG_0586-2.jpg"
        _remove_if_exist(output_path)
        cat_detector = Cat_Detector()
        image_path = "/workdir/tests/data/resized/IMG_0586-2.jpg"
        assert not os.path.exists(output_path)
        cat_detector.move_if_detection_is_positive(image_path, "/workdir/tests/data")
        assert os.path.exists(output_path)
        _remove_if_exist(output_path)


def _remove_if_exist(path):
    if os.path.exists(path):
        os.remove(path)
