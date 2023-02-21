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
    new_name = "image3_resized.jpg"
    cr.try_resize_image(original_image_path, resized_image_path, new_name, photos_with_error)
    assert len(photos_with_error) == 1


expected_paths = [
    "/workdir/tests/data/photo_with_error.JPG",
    "/workdir/tests/data/image3_resized.jpg",
    "/workdir/tests/data/image3.jpg",
    "/workdir/tests/data/processed/cat_detected/image3_predicted.jpg",
    "/workdir/tests/data/processed/no_cat_detected/IMG_0178_predicted.jpg",
    "/workdir/tests/data/resized/image3.jpg",
]


def tests_obtain_recursive_paths():
    root_path = "/workdir/tests/data/"
    obtained_paths = cr.obtain_recursive_paths(root_path)
    assert obtained_paths == expected_paths


expected_names = [
    "photo_with_error.JPG",
    "image3_resized.jpg",
    "image3.jpg",
    "processed_cat_detected_image3_predicted.jpg",
    "processed_no_cat_detected_IMG_0178_predicted.jpg",
    "resized_image3.jpg",
]


def tests_obtain_output_names():
    root_path = "/workdir/tests/data/"
    obtained_names = cr.obtain_output_names(root_path)
    assert obtained_names == expected_names
