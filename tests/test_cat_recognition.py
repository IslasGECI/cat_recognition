import hashlib
import os

import cat_recognition as cr


def test_resize_image():
    original_image_path = "tests/data/image3.jpg"
    resized_image_path = "tests/data/image3_resized.jpg"
    cr.resize_image(original_image_path, resized_image_path)
    assert os.path.isfile(resized_image_path)

    image = open(resized_image_path, "rb").read()
    obtained_hash = hashlib.md5(image).hexdigest()
    expected_hash = "12f1ac191833ce9a8ad3e9482545176d"
    assert obtained_hash == expected_hash


def test_try_resize_image():
    photos_with_error = []
    original_image_path = "/workdir/tests/data/photo_with_error.JPG"
    resized_image_path = "tests/data/image3_resized.jpg"
    try_resize_image(original_image_path, resized_image_path, photos_with_error)
    assert len(photos_with_error) == 1
