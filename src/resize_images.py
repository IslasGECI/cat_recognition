import os
from tqdm import tqdm

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


original_images_path = "/workdir/data/raw/photos/"
resized_image_path = "/workdir/data/resized/"
images_list = [original_images_path + file_name for file_name in os.listdir(original_images_path)]

error_photos = []
if not os.path.exists(resized_image_path):
    os.mkdir(resized_image_path)
images_list_bar = tqdm(images_list)
for image in images_list_bar:
    try:
        resize_image(image, os.path.join(resized_image_path, os.path.split(image)[1]))
    except:
        error_photos.append(image)

print("fotos con errores:")
[print(foto) for foto in error_photos]
