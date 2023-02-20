from os import listdir
from cat_recognition.yolo_detections import classify_from_path, Net_Yolo, is_there_a_cat

net_yolo = Net_Yolo()


def move_photo_with_detections(files):
    print(files)


# Load Image
images = listdir("data/resized/")
all_paths = [f"/workdir/data/resized/{image}" for image in images]
all_outs = [classify_from_path(image_path, net_yolo) for image_path in all_paths]
for files, outs in zip(all_paths, all_outs):
    if is_there_a_cat(outs):
        move_photo_with_detections(files)
