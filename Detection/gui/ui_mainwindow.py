# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1550, 900)
        MainWindow.setMinimumSize(QSize(1550, 900))
        MainWindow.setMaximumSize(QSize(1550, 900))
        self.actionResim_A = QAction(MainWindow)
        self.actionResim_A.setObjectName(u"actionResim_A")
        self.actionVideo_A = QAction(MainWindow)
        self.actionVideo_A.setObjectName(u"actionVideo_A")
        self.actionKaydet = QAction(MainWindow)
        self.actionKaydet.setObjectName(u"actionKaydet")
        self.actionDosyay_Kapat = QAction(MainWindow)
        self.actionDosyay_Kapat.setObjectName(u"actionDosyay_Kapat")
        self.actionProgramdan_k = QAction(MainWindow)
        self.actionProgramdan_k.setObjectName(u"actionProgramdan_k")
        self.actionVeri_D_zenleme = QAction(MainWindow)
        self.actionVeri_D_zenleme.setObjectName(u"actionVeri_D_zenleme")
        self.actionModel_E_itimi = QAction(MainWindow)
        self.actionModel_E_itimi.setObjectName(u"actionModel_E_itimi")
        self.actionYard_m = QAction(MainWindow)
        self.actionYard_m.setObjectName(u"actionYard_m")
        self.actionHakk_nda = QAction(MainWindow)
        self.actionHakk_nda.setObjectName(u"actionHakk_nda")
        self.actionAyarlar = QAction(MainWindow)
        self.actionAyarlar.setObjectName(u"actionAyarlar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 0, 741, 631))
        self.kaynak = QLabel(self.groupBox_3)
        self.kaynak.setObjectName(u"kaynak")
        self.kaynak.setGeometry(QRect(10, 20, 720, 600))
        self.kaynak.setMinimumSize(QSize(720, 600))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(760, 0, 781, 631))
        self.sonuc = QLabel(self.groupBox_4)
        self.sonuc.setObjectName(u"sonuc")
        self.sonuc.setGeometry(QRect(10, 20, 720, 600))
        self.sonuc.setMinimumSize(QSize(720, 600))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 630, 961, 221))
        self.model_type = QComboBox(self.groupBox)
        self.model_type.setObjectName(u"model_type")
        self.model_type.setGeometry(QRect(100, 20, 80, 20))
        self.model_type.setMinimumSize(QSize(80, 20))
        self.model_type.setMaximumSize(QSize(80, 20))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 61, 16))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 20, 81, 20))
        self.metin_kaynak = QLineEdit(self.groupBox)
        self.metin_kaynak.setObjectName(u"metin_kaynak")
        self.metin_kaynak.setGeometry(QRect(280, 20, 321, 20))
        self.b_kaynak_ac = QPushButton(self.groupBox)
        self.b_kaynak_ac.setObjectName(u"b_kaynak_ac")
        self.b_kaynak_ac.setGeometry(QRect(610, 20, 75, 23))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(21, 50, 61, 16))
        self.model_size = QComboBox(self.groupBox)
        self.model_size.setObjectName(u"model_size")
        self.model_size.setGeometry(QRect(100, 50, 80, 20))
        self.model_size.setMinimumSize(QSize(80, 20))
        self.model_size.setMaximumSize(QSize(80, 20))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 50, 81, 20))
        self.b_hedef_ac = QPushButton(self.groupBox)
        self.b_hedef_ac.setObjectName(u"b_hedef_ac")
        self.b_hedef_ac.setGeometry(QRect(610, 50, 75, 23))
        self.metin_hedef = QLineEdit(self.groupBox)
        self.metin_hedef.setObjectName(u"metin_hedef")
        self.metin_hedef.setGeometry(QRect(280, 50, 321, 20))
        self.cuda_kullan = QCheckBox(self.groupBox)
        self.cuda_kullan.setObjectName(u"cuda_kullan")
        self.cuda_kullan.setGeometry(QRect(25, 80, 151, 20))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(980, 630, 561, 221))
        self.textEdit = QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 20, 541, 131))
        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 160, 541, 23))
        self.progressBar.setValue(0)
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 190, 502, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.curr_frame_counter = QLineEdit(self.widget)
        self.curr_frame_counter.setObjectName(u"curr_frame_counter")
        self.curr_frame_counter.setEnabled(False)

        self.horizontalLayout.addWidget(self.curr_frame_counter)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.total_frame_counter = QLineEdit(self.widget)
        self.total_frame_counter.setObjectName(u"total_frame_counter")
        self.total_frame_counter.setEnabled(False)

        self.horizontalLayout.addWidget(self.total_frame_counter)

        self.pb2 = QPushButton(self.widget)
        self.pb2.setObjectName(u"pb2")

        self.horizontalLayout.addWidget(self.pb2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1550, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0130stenmeyen Nesne Tespiti Uygulamas\u0131", None))
        self.actionResim_A.setText(QCoreApplication.translate("MainWindow", u"Resim A\u00e7", None))
        self.actionVideo_A.setText(QCoreApplication.translate("MainWindow", u"Video A\u00e7", None))
        self.actionKaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.actionDosyay_Kapat.setText(QCoreApplication.translate("MainWindow", u"Dosyay\u0131 Kapat", None))
        self.actionProgramdan_k.setText(QCoreApplication.translate("MainWindow", u"Programdan \u00c7\u0131k", None))
        self.actionVeri_D_zenleme.setText(QCoreApplication.translate("MainWindow", u"Veri D\u00fczenleme", None))
        self.actionModel_E_itimi.setText(QCoreApplication.translate("MainWindow", u"Model E\u011fitimi", None))
        self.actionYard_m.setText(QCoreApplication.translate("MainWindow", u"Yard\u0131m", None))
        self.actionHakk_nda.setText(QCoreApplication.translate("MainWindow", u"Hakk\u0131nda", None))
        self.actionAyarlar.setText(QCoreApplication.translate("MainWindow", u"Ayarlar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Kaynak", None))
        self.kaynak.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0130\u015flenmi\u015f", None))
        self.sonuc.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ayarlar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Yolo Model:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kaynak Dosya:", None))
        self.b_kaynak_ac.setText(QCoreApplication.translate("MainWindow", u"A\u00e7", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Model Size:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hedef Dosya:", None))
        self.b_hedef_ac.setText(QCoreApplication.translate("MainWindow", u"A\u00e7", None))
        self.cuda_kullan.setText(QCoreApplication.translate("MainWindow", u"CUDA Destekli Hesapla", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0130\u015fleme", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Frame:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Frame:", None))
        self.pb2.setText(QCoreApplication.translate("MainWindow", u"Ba\u015fla", None))
    # retranslateUi

