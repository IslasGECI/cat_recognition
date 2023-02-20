import cv2 as cv
from os import listdir
from cat_recognition.yolo_detections import classify_from_path, Net_Yolo, is_there_a_cat

# load yolo
net = cv.dnn.readNet("/workdir/yolov3.weights", "/workdir/darknet/cfg/yolov3.cfg")
with open("/workdir/darknet/data/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
# print(classes)
layer_name = net.getLayerNames()
output_layer = [layer_name[i - 1] for i in net.getUnconnectedOutLayers()]

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
