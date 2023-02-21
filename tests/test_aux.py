import os
import cat_recognition as cr


def test_mkdir_resized_image_path():
    cr.mkdir_resized_image_path()
    assert os.path.exists("data/resized")