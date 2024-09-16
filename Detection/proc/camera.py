import cv2
from PySide6.QtCore import QRunnable, Slot
from Detection.proc.signals import ProcessSignals
from Detection.proc.utils import cv2qimage, cv2label, cv2blur, cv2rect
from Detection.proc.yolo_detector import YOLODetector


class VideoProcessor(QRunnable):
    def __init__(self, model_type, model_weights, device):
        super(VideoProcessor, self).__init__()
        self.model_type = model_type
        self.model_weights = model_weights
        self.device = device

        self.video_capture = cv2.VideoCapture(0)  # Kameradan video yakalama
        self.frame_width = int(self.video_capture.get(3))
        self.frame_height = int(self.video_capture.get(4))
        self.fps = 30  # Varsayılan olarak 30 FPS

        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.output_file = "output_camera_video.mp4"  # Çıkış dosya adı
        self.video_writer = cv2.VideoWriter(self.output_file,
                                            self.fourcc,
                                            self.fps,
                                            (self.frame_width, self.frame_height))

        self.current_frame = 0
        self.total_frames = 0
        self.signals = ProcessSignals()
        self.bluring = True
        self.labeling = True

    def set_processing(self, is_bluring, is_labeling):
        self.bluring = is_bluring
        self.labeling = is_labeling

    @Slot()
    def run(self):
        yolo = YOLODetector(self.model_type, self.model_weights, self.device)
        while True:
            success, frame = self.video_capture.read()  # Kameradan görüntü al
            if success:
                self.current_frame += 1
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
                self.signals.progress.emit(cv2qimage(frame), cv2qimage(processed_frame), self.current_frame,
                                           self.total_frames)
                # buraya bir çıkma komutu ekle
                #if keyboard.is_pressed('q'):
                    #break
            else:
                self.signals.error.emit("Error while reading video frame...")
                break
        self.video_writer.release()
        self.video_capture.release()
        self.signals.finished.emit("Finished...")
