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


def try_resize_image(original_path: str, destionation_path: str, new_name: str, error_photos: list):
    try:
        destionation_path = os.path.join(destionation_path, new_name)
        resize_image(
            original_path, destionation_path)
    except:
        error_photos.append(original_path)


def obtain_recursive_paths(root_path: str):
    all_paths = []
    for root, _, files in os.walk(root_path):
        for name in files:
            all_paths.append(os.path.join(root, name))
    return all_paths


def obtain_output_names(root_path):
    recursive_paths = obtain_recursive_paths(root_path)
    return [path.split(root_path)[-1].replace("/", "_") for path in recursive_paths]
