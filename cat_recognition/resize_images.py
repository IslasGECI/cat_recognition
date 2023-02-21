import os
from PIL import Image


def resize_image(
    original_path: str,
    destionation_path: str,
    width: int = 512,
    height: int = 512,
    scale_filter=Image.ANTIALIAS,
):
    original_image = Image.open(original_path)
    resized_image = original_image.resize((width, height), scale_filter)
    resized_image.save(destionation_path)


def try_resize_image(original_path: str, destionation_path: str, error_photos: list):
    try:
        resize_image(
            original_path, os.path.join(destionation_path, os.path.split(original_path)[1])
        )
    except:
        error_photos.append(original_path)


def obtain_recursive_paths(root_path: str):
    all_paths = []
    for root, _, files in os.walk(root_path):
        for name in files:
            all_paths.append(os.path.join(root, name))
    return all_paths
