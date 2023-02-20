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


original_images_path = "/workdir/data/raw/"
resized_image_path = "/workdir/data/resized/"
images_list = [original_images_path + file_name for file_name in os.listdir(original_images_path)]

if not os.path.exists(resized_image_path):
    os.mkdir(resized_image_path)

for image in images_list:
    resize_image(image, os.path.join(resized_image_path, os.path.split(image)[1]))
