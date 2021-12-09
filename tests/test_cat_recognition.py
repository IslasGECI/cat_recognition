import cat_recognition as cr
import os


def test_resize_image():
    original_image_path = "tests/data/image3.jpg"
    resized_image_path = "tests/data/image3_resized.jpg"
    cr.resize_image(original_image_path, resized_image_path)
    assert os.path.isfile(resized_image_path)
