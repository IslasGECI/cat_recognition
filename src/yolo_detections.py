from tqdm import tqdm
from os import listdir, path, mkdir, replace
from cat_recognition.yolo_detections import classify_from_path, Net_Yolo, is_there_a_cat

net_yolo = Net_Yolo()


def move_photo_with_detections(files):
    if not path.exists("/workdir/data/cat_detected/"):
        mkdir("/workdir/data/cat_detected/")
    old_path = f"/workdir/data/resized/{files}"
    new_path = f"/workdir/data/cat_detected/{files}"
    replace(old_path, new_path)
    print(files)


# Load Image
images = listdir("data/resized/")
all_paths = [f"/workdir/data/resized/{image}" for image in images]
all_outs = [classify_from_path(image_path, net_yolo) for image_path in tqdm(all_paths)]
for image, outs in zip(images, all_outs):
    if is_there_a_cat(outs):
        move_photo_with_detections(image)
