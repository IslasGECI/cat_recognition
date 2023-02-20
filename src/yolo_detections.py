import cv2 as cv
import numpy as np

# load yolo
net = cv.dnn.readNet("/workdir/yolov3.weights", "/workdir/darknet/cfg/yolov3.cfg")
clasees = []
with open("/workdir/darknet/data/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
# print(classes)
layer_name = net.getLayerNames()
output_layer = [layer_name[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Load Image
images = [
    "IMG_0063.jpg",
    "IMG_0178.jpg",
    "IMG_0269.jpg",
    "IMG_0270.jpg",
    "IMG_0348.jpg",
    "IMG_0586.jpg",
    "IMG_0588.jpg",
]
img = cv.imread(f"/workdir/data/resized/{images[0]}")
height, width, channel = img.shape

# Detect Objects
blob = cv.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layer)

class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]  # Tiramos algunos "objetos" ¿Por qué no están el coco.name?
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.01:
            # Object detection
            confidences.append(float(confidence))
            class_ids.append(class_id)


for class_id in class_ids:
    print(classes[class_id])
