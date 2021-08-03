# - * - coding: UTF - 8 -*-
import cv2 as cv
import numpy as np


class YOLO:
    def __init__(self, cfg, weights, image_resize):
        self.image_resize = image_resize
        self.net = cv.dnn.readNetFromDarknet(cfg, weights)
        self.net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)  # cv.dnn.DNN_BACKEND_INFERENCE_ENGINE
        self.net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)  # 切换到GPU：cv.dnn.DNN_TARGET_OPENCL (only Intel GPU)

    # Load names of classes
    classesFile = "model/coco.names"
    classes = None
    with open(classesFile, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')

    def detect(self, frame, conf_thresh=0.25, nmsThreshold=0.45):
        if frame is None:
            return None
        blob = cv.dnn.blobFromImage(frame, 1 / 255, self.image_resize, [0, 0, 0], 1, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.getOutputsNames())  # 网络前向计算
        result = self.postprocess(frame, outs, conf_thresh, nmsThreshold)
        return result

    def postprocess(self, frame, outs, conf_thresh, nmsThreshold):
        # Remove the bounding boxes with low confidence using non-maxima suppression
        frameHeight = frame.shape[0]
        frameWidth = frame.shape[1]

        classIds, confidences, boxes = [], [], []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > conf_thresh:
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)
                    classIds.append(classId)
                    confidences.append(float(confidence))
                    boxes.append([left, top, width, height])

        # Perform non maximum suppression to eliminate redundant overlapping boxes with lower confidences.
        indices = cv.dnn.NMSBoxes(boxes, confidences, conf_thresh, nmsThreshold)

        result = []
        labels = []
        for i in indices:
            i = i[0]
            box = np.array(boxes[i])
            box[box < 0] = 0
            xmin, ymin, xmax, ymax = box[0], box[1], box[0] + box[2], box[1] + box[3]
            label = self.classes[classIds[i]]
            labels.append(label)
            obj = [xmin, ymin, xmax, ymax, confidences[i]]
            result.append(obj)

        return np.array(result), labels

    def getOutputsNames(self):
        # Get the names of the net output layers
        layersNames = self.net.getLayerNames()
        return [layersNames[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
