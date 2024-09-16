import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile, Qt, QRunnable, Slot, QThreadPool 
from PySide6.QtGui import QImage, QPixmap

from gui.ui_mainwindow import Ui_MainWindow
from Detection.proc.video import VideoProcessor
from Detection.proc.utils import is_cuda_available

   

class MainWindow(QMainWindow): 

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        self.set_window_interface()

    def set_window_interface(self):
        self.setFixedSize(self.width(), self.height())
        self.ui.model_type.insertItem(0,"yolov5")
        self.ui.model_type.insertItem(1,"yolov8")

        self.ui.model_size.insertItem(0,"Nano")
        self.ui.model_size.insertItem(1,"Small")
        self.ui.model_size.insertItem(2,"Medium")
        self.ui.model_size.insertItem(3,"Large")
        self.ui.model_size.insertItem(4,"XLarge")

        self.ui.cuda_kullan.setEnabled(is_cuda_available())
        self.ui.cuda_kullan.setChecked(is_cuda_available())

        self.ui.b_kaynak_ac.clicked.connect(self.open_source_file)
        self.ui.b_hedef_ac.clicked.connect(self.open_dest_file)
        self.ui.pb2.clicked.connect(self.run_process)

    def open_source_file(self):
        self.input_file, _ = QFileDialog.getOpenFileName(None, 
                                                "Resim ve Video Dosyaları Aç", 
                                                ".", 
                                                "*.jpg;*jpeg;*.png;*.mp4")
        self.ui.metin_kaynak.setText(self.input_file)

    def open_dest_file(self):
        self.output_file, _ = QFileDialog.getSaveFileName(None,
                                                          "İşlenecek Dosyayı Kaydet",
                                                          ".",
                                                          "*.jpg;*jpeg;*.png;*.mp4")
        self.ui.metin_hedef.setText(self.output_file) 


    def run_process(self):
        model_type = self.ui.model_type.currentText()
        model_weights = f"models/sigarav8s.pt"
        model_type_index = self.ui.model_type.currentIndex()
        model_size_index = self.ui.model_size.currentIndex()

        if model_type_index == 1:
            if model_size_index == 0:
                model_weights = f"models/sigarav8n.pt"
            elif model_size_index == 1:
                model_weights = f"models/sigarav8s.pt"
            elif model_size_index == 2:
                model_weights = f"models/sigarav8m.pt"
            elif model_size_index == 3:
                model_weights = f"models/sigarav8l.pt"
            elif model_size_index == 4:
                model_weights = f"models/sigarav8x.pt"
        elif model_type_index == 0:
            if model_size_index == 0:
                model_weights = f"models/sigarav5n.pt"
            elif model_size_index == 1:
                model_weights = f"models/sigarav5s.pt"
            elif model_size_index == 2:
                model_weights = f"models/sigarav5m.pt"
            elif model_size_index == 3:
                model_weights = f"models/sigarav5l.pt"
            elif model_size_index == 4:
                model_weights = f"models/sigarav5x.pt"

        # GPU mu CPU mu seçimini ayarlar
        if self.ui.cuda_kullan.isChecked():
            device = "cuda:0"
        else:
            device = "cpu"

        video = VideoProcessor(self.input_file, 
                               self.output_file, 
                               model_type, 
                               model_weights,
                               device)
        self.total_frame_count = video.getTotalFrameCount()
        self.ui.total_frame_counter.setText( str(self.total_frame_count))
        
        video.signals.error.connect(self.process_error) 
        video.signals.progress.connect(self.process_update)   
        video.signals.finished.connect(self.process_finished) 
        self.threadpool.start(video)

    def process_error(self, str):
        print(str)

    def process_update(self, image, processed_image, current, total):

        self.ui.kaynak.setPixmap(
            image.scaled(
                self.ui.kaynak.width(),
                self.ui.kaynak.height(),
                Qt.KeepAspectRatio)
            )
        
        self.ui.sonuc.setPixmap(
            processed_image.scaled(
                self.ui.sonuc.width(),
                self.ui.sonuc.height(),
                Qt.KeepAspectRatio)
            )
        
        self.ui.curr_frame_counter.setText(str(current))

        percentage = int((current * 100 ) /self.total_frame_count)
        self.ui.progressBar.setValue(percentage)

    def process_finished(str):
        print(str)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    sys.exit(app.exec())