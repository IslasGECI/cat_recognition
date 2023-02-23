from tqdm import tqdm
from os import listdir, path, mkdir, replace
from cat_recognition.yolo_detections import (
    classify_from_path,
    Net_Yolo,
    is_there_a_cat,
    move_photo_with_detections,
)

net_yolo = Net_Yolo()


# Load Image
images = listdir("data/resized/")
all_paths = [f"/workdir/data/resized/{image}" for image in images]
all_outs = [classify_from_path(image_path, net_yolo) for image_path in tqdm(all_paths)]
for image, outs in zip(images, all_outs):
    if is_there_a_cat(outs):
        move_photo_with_detections(image, "/workdir/data")
