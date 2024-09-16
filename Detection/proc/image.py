import cv2
from pathlib import Path
from Detection.proc.signals import ProcessSignals
from Detection.proc.utils import cv2qimage, cv2label, cv2blur, cv2rect
from Detection.proc.yolo_detector import YOLODetector

class ImageProcessor:
    def __init__(self, model_type, model_weights, device):
        self.model_type = model_type
        self.model_weights = model_weights
        self.device = device
        self.current_frame = 0
        self.total_frames = 0
        self.signals = ProcessSignals()
        self.bluring = True
        self.labeling = True

    def set_processing(self, is_bluring, is_labeling):
        self.bluring = is_bluring
        self.labeling = is_labeling

    def run(self, image_paths):
        yolo = YOLODetector(self.model_type, self.model_weights, self.device)
        for image_path in image_paths:
            frame = cv2.imread(str(image_path))
            prediction_list = yolo.predict_frame(frame)
            processed_frame = frame.copy()
            for index, _ in enumerate(prediction_list):
                x1 = int(prediction_list[index].bbox.minx)
                y1 = int(prediction_list[index].bbox.miny)
                x2 = int(prediction_list[index].bbox.maxx)
                y2 = int(prediction_list[index].bbox.maxy)
                label = prediction_list[index].category.name
                if self.bluring:
                    cv2blur(processed_frame, x1, x2, y1, y2, 30)
                if self.labeling:
                    cv2rect(processed_frame, x1, x2, y1, y2)
                    cv2label(processed_frame, x1, x2, y1, y2, label)
            yield cv2qimage(frame), cv2qimage(processed_frame)
