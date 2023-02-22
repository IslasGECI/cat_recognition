import os
import shutil
import cat_recognition as cr


def test_mkdir_resized_image_path():
    resized_image_path = "/workdir/data/resized"
    if os.path.exists(resized_image_path):
        shutil.rmtree(resized_image_path)
    cr.mkdir_resized_image_path()
    assert os.path.exists(resized_image_path)
