from PIL import Image


def resize_image(original_path: str, destionation_path: str, width: int = 256,
                 height: int = 256, scale_filter=Image.ANTIALIAS):
    original_image = Image.open(original_path)
    resized_image = original_image.resize((width, height), scale_filter)
    resized_image.save(destionation_path)


if __name__ == "__main__":
    # Here we suppose that the images are in the root of the repository
    # in the folder called data/originals
    import os

    original_images_path = "./data/originals/"
    resized_image_path = "./data/resized/"
    images_list = [original_images_path +
                   file_name for file_name in os.listdir(original_images_path)]

    if not os.path.exists(resized_image_path):
        os.mkdir(resized_image_path)

    for image in images_list:
        resize_image(image, os.path.join(
            resized_image_path, os.path.split(image)[1]))
