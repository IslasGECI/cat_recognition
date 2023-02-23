import cv2 as cv


def classify_from_path(image_path, Net):
    img = cv.imread(image_path)
    blob = cv.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    Net.set_input(blob)
    return Net.forward()


def is_there_a_cat(outs, cut_prob = 0.01):
    for out in outs:
        for detection in out:
            scores = detection[5:]
            cat_id = 15
            cat_confidence = scores[cat_id]
            if cat_confidence > cut_prob:
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

def move_photo_with_detections():
    pass