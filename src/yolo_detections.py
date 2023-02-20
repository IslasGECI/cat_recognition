import cv2 as cv
from os import listdir

# load yolo
net = cv.dnn.readNet("/workdir/yolov3.weights", "/workdir/darknet/cfg/yolov3.cfg")
clasees = []
with open("/workdir/darknet/data/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
# print(classes)
layer_name = net.getLayerNames()
output_layer = [layer_name[i - 1] for i in net.getUnconnectedOutLayers()]

# Load Image
images = listdir("data/resized/")
image_path = f"/workdir/data/resized/{images[6]}"
def clasify_from_path(image_path):
    img = cv.imread(image_path)
    blob = cv.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    return net.forward(output_layer)

outs = clasify_from_path(image_path)
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
