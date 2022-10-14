import os

from cat_recognition import resize_image

original_images_path = "./data/raw/"
resized_image_path = "./data/resized/"
images_list = [original_images_path + file_name for file_name in os.listdir(original_images_path)]

if not os.path.exists(resized_image_path):
    os.mkdir(resized_image_path)

    for image in images_list:
        resize_image(image, os.path.join(resized_image_path, os.path.split(image)[1]))
