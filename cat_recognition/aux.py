import os


def mkdir_resized_image_path():
    resized_image_path = "/workdir/data/resized"
    if not os.path.exists(resized_image_path):
        os.mkdir(resized_image_path)