from os import path, mkdir, replace
import cv2 as cv


def classify_from_path(image_path, Net):
    img = cv.imread(image_path)
    blob = transform_image_to_blob(img)
    Net.set_input(blob)
    return Net.forward()


def is_there_a_cat(outs, cut_prob=0.01):
    for out in outs:
        for detection in out:
            scores = detection[5:]
            cat_id = 15
            cat_confidence = scores[cat_id]
            if cat_confidence > cut_prob:
                return True


def is_there_a_mammals(outs, cut_prob=0.01):
    for out in outs:
        for detection in out:
            mammals_confidence = detection[20:29]
            detected_mammal = [mammal > cut_prob for mammal in mammals_confidence]
            if any(detected_mammal):
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


def move_photo_with_detections(files, path_data):
    if not path.exists(f"{path_data}/cat_detected/"):
        mkdir(f"{path_data}/cat_detected/")
    old_path = f"{path_data}/resized/{files}"
    new_path = f"{path_data}/cat_detected/{files}"
    replace(old_path, new_path)
    print(files)


def transform_image_to_blob(img):
    return cv.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True)
