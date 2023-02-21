import os
from tqdm import tqdm


from cat_recognition import try_resize_image

original_images_path = "/workdir/data/raw/photos/"
resized_image_path = "/workdir/data/resized/"
images_list = [original_images_path + file_name for file_name in os.listdir(original_images_path)]

error_photos = []
if not os.path.exists(resized_image_path):
    os.mkdir(resized_image_path)
images_list_bar = tqdm(images_list)
for image in images_list_bar:
    try_resize_image(image, resized_image_path, error_photos)

print("fotos con errores:")
[print(foto) for foto in error_photos]
