import os
from tqdm import tqdm


from cat_recognition import try_resize_image, mkdir_resized_image_path, obtain_recursive_paths, obtain_output_names

original_images_path = "/workdir/data/raw/photos/"
resized_image_path = "/workdir/data/resized/"
images_list = obtain_recursive_paths(original_images_path)
new_names = obtain_output_names(original_images_path)

error_photos = []
mkdir_resized_image_path()
images_list_bar = tqdm(images_list)
for image, new_name in zip(images_list_bar, new_names):
    try_resize_image(image, resized_image_path, new_name, error_photos)

print("fotos con errores:")
[print(foto) for foto in error_photos]
