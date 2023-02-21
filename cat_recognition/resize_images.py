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
    pass