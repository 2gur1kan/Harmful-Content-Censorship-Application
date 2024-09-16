from PySide6.QtCore import QRunnable, Slot
import cv2

from Detection.proc.signals import ProcessSignals
from Detection.proc.utils import cv2qimage, cv2label, cv2blur, cv2rect
from Detection.proc.yolo_detector import YOLODetector

class VideoProcessor(QRunnable):

    def __init__(self, input_file, output_file, model_type, model_weights, device):
        super(VideoProcessor, self).__init__() 
        self.model_type = model_type
        self.model_weights = model_weights
        self.device = device
        self.input_file = input_file
        self.video_capture = cv2.VideoCapture(self.input_file) 
        self.frame_width = int(self.video_capture.get(3))
        self.frame_height = int(self.video_capture.get(4))
        self.fps = int(self.video_capture.get(5))

        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.output_file = output_file
        self.video_writer = cv2.VideoWriter(self.output_file, 
                                       self.fourcc, 
                                       self.fps, 
                                       (self.frame_width, self.frame_height))
        
        self.currentframe = 0
        self.totalframes =  int (self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.signals = ProcessSignals() 
        self.bluring = True
        self.labeling = True

    def getTotalFrameCount(self):
        return self.totalframes

    def setProcessing(self, isBluring, isLabeling):
        self.bluring = isBluring
        self.labeling = isLabeling

    @Slot()
    def run(self): 
        yolo = YOLODetector(self.model_type, self.model_weights, self.device)
        while self.video_capture.isOpened():
            success, frame = self.video_capture.read()
            if success: 
                self.currentframe = self.currentframe + 1
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
                self.video_writer.write(processed_frame)
                self.signals.progress.emit(cv2qimage(frame), cv2qimage(processed_frame), self.currentframe, self.totalframes)
            else:
                self.signals.error.emit("Error while reading video file...")
                break
        self.video_writer.release()
        self.video_capture.release()
        self.signals.finished.emit("Finished...")