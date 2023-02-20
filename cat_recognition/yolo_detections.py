import cv2 as cv


def classify_from_path(image_path, Net):
    img = cv.imread(image_path)
    blob = cv.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    Net.set_input(blob)
    return Net.forward()


def is_there_a_cat(outs):
    for out in outs:
        for detection in out:
            scores = detection[5:]  # Tiramos algunos "objetos" ¿Por qué no están el coco.name?
            class_id = 15  # np.argmax(scores)
            cat_confidence = scores[class_id]
            # print(cat_confidence)
            if cat_confidence > 0.01:
                # Object detection
                return True


class Net_Yolo:
    def __init__(self):
        self.net = cv.dnn.readNet("/workdir/yolov3.weights", "/workdir/darknet/cfg/yolov3.cfg")
        layer_name = self.net.getLayerNames()
        self.output_layer = [layer_name[i - 1] for i in self.net.getUnconnectedOutLayers()]

    def set_input(self, blob):
        self.net.setInput(blob)

    def forward(self):
        return self.net.forward(self.output_layer)