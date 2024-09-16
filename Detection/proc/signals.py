from PySide6.QtGui import QPixmap
from PySide6.QtCore import QObject, Signal

class ProcessSignals(QObject):
    error = Signal(str) 
    progress = Signal(QPixmap, QPixmap, int, int)
    finished = Signal(str)