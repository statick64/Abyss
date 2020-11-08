# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abyss.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal
import ui.resources
import sys
from ui.popup import *
from engine.downloads import VideoDownloader
import youtube_dl
import requests
import os


class Ui_Abyss(object):


    def download_clicked(self):
        self.window = QtWidgets.QDialog()
        url = self.input_text.toPlainText()
        self.VideoDownloader = VideoDownloader(url)
        self.ui = Ui_Add(url)
        self.ui.setupUi(self.window)
        self.window.show()

    class Worker(QObject):
        progressChanged = pyqtSignal(int)

        def my_hook(self, d):
            if d['status'] == 'finished':
                file_tuple = os.path.split(os.path.abspath(d['filename']))
                print("Done downloading {}".format(file_tuple[1]))
            if d['status'] == 'downloading':
                p = d['_percent_str'][:3]
                self.progressChanged.emit(int(p))

        def download(self, song):
            ydl_opts = {
                'format': '133',
                'progress_hooks': [self.my_hook],
            }

            ydl = youtube_dl.YoutubeDL(ydl_opts)
            ydl.download([song])

    def download_clicker(self):
        self.widget.setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        url = self.input_text.toPlainText()
        vid = VideoDownloader(url)
        self.set_size = vid.formated_size()
        self.set_title = vid.video_title()
        self.title.setText(self.set_title)
        self.size.setText(self.set_size)
        worker = Worker()
        thread = QThread()
        worker.moveToThred(thread)
        worker.progressChanged.connect(progressBar.setValue)
        thread.started.connect(worker.download(url))
        thread.start()

    


    def user_404(self):
        self.Body.setVisible(False)
        self.Converter_404.setVisible(False)
        self.User_404.setVisible(True)

    def convert_404(self):
        self.Body.setVisible(False)
        self.User_404.setVisible(False)
        self.Converter_404.setVisible(True)

    def download_page(self):
        self.User_404.setVisible(False)
        self.Body.setVisible(True)
        self.Converter_404.setVisible(False)

    def side_bottuns(self):
        if self.Download_side_button.clicked:
            self.User_404.setVisible(False)
            self.Body.setVisible(True)
            self.Converter_404.setVisible(False)
        elif self.Converter_side_button.clicked:
            self.Body.setVisible(False)
            self.User_404.setVisible(False)
            self.Converter_404.setVisible(True)
        elif self.User_side_button.clicked:
            self.Body.setVisible(False)
            self.Converter_404.setVisible(False)
            self.User_404.setVisible(True)

    def setupUi(self, Abyss):
        Abyss.setObjectName("Abyss")
        Abyss.resize(772, 519)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(Abyss.sizePolicy().hasHeightForWidth())
        Abyss.setSizePolicy(sizePolicy)
        Abyss.setSizeIncrement(QtCore.QSize(0, 4))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        Abyss.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/widow_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Abyss.setWindowIcon(icon)
        Abyss.setWindowOpacity(1.0)
        Abyss.setLayoutDirection(QtCore.Qt.LeftToRight)
        Abyss.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                            "QFontDatabase fontDatabase; \n"
                            "fontDatabase.addApplicationFont(\"C:\\Users\\Kenne\\Desktop\\images\\Quicksand-VariableFont_wght.ttf\");")
        Abyss.setIconSize(QtCore.QSize(24, 22))
        self.centralwidget = QtWidgets.QWidget(Abyss)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.Body = QtWidgets.QFrame(self.centralwidget)
        self.Body.setGeometry(QtCore.QRect(180, 0, 661, 520))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy)
        self.Body.setVisible(True)
        self.Body.setStyleSheet("background-color: #ECF3FA; ")
        self.Body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Body.setObjectName("Body")
        self.Body_header = QtWidgets.QLabel(self.Body)
        self.Body_header.setGeometry(QtCore.QRect(40, 10, 191, 51))
        self.Body_header.setStyleSheet("font-weight: 200;\n"
                                       "font-size: 24px;\n"
                                       "line-height: 45px;\n"
                                       "color: #034460;\n"
                                       "border:none;")
        self.Body_header.setLineWidth(4)
        self.Body_header.setObjectName("Body_header")
        self.header2 = QtWidgets.QLabel(self.Body)
        self.header2.setGeometry(QtCore.QRect(40, 126, 71, 20))
        self.header2.setStyleSheet("font-weight: 200;\n"
                                   "font-size: 14px;\n"
                                   "line-height: 35px;\n"
                                   "color: #034460;\n"
                                   "border:none;")
        self.header2.setObjectName("header2")
        self.download_button = QtWidgets.QPushButton(self.Body)
        self.download_button.setGeometry(QtCore.QRect(440, 70, 121, 31))
        self.download_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_button.setStyleSheet("border-radius: 4px;\n"
                                           "background: #034460; \n"
                                           "color: #FFFFFF;\n"
                                           "font-size: 14px;")
        self.download_button.setObjectName("download_button")
        self.download_button.clicked.connect(self.download_clicker)
        self.input_text = QtWidgets.QPlainTextEdit(self.Body)
        self.input_text.setGeometry(QtCore.QRect(40, 70, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.input_text.sizePolicy().hasHeightForWidth())
        self.input_text.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.input_text.setPalette(palette)
        self.input_text.setAutoFillBackground(True)
        self.input_text.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                      "border-radius: 4px;\n"
                                      "border: 1px solid #D9D9D9;\n"
                                      "box-sizing: border-box;\n"
                                      "padding-left: 20px;\n"
                                      "color: black;\n"
                                      "padding-top:4px;")
        self.input_text.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_text.setLineWidth(12)
        self.input_text.setPlainText("")
        self.input_text.setBackgroundVisible(True)
        self.input_text.setObjectName("input_text")
        self.frame = QtWidgets.QFrame(self.Body)
        self.frame.setGeometry(QtCore.QRect(40, 160, 521, 321))
        self.frame.setStyleSheet("border : 1px solid #D9D9D9;\n"
                                 "background-color: white;\n"
                                 "border-radius: 4px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 521, 41))
        self.widget.setStyleSheet("QWidget{\n"
                                  "\n"
                                  "background-color: white;}\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.widget.setVisible(True)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 16, 20))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setStyleSheet("QCheckBox::chunck {\n"
                                    "border-raduis:4px;\n"
                                    "border: 1px solid #D9D9D9;\n"
                                    "}\n"
                                    "QCheckBox{"
                                    "border: none;\n}")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(260, 10, 118, 21))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("QProgressBar::chunk   {\n"
                                       "background-color:#034460; \n"
                                       "border-radius: 4px\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar {\n"
                                       "border-radius:4px;\n"
                                       "border:1px solid #F2F2F2;\n"
                                       "background-color: #F2F2F2;\n"
                                       "text-align:center;\n"
                                       "text-size: 3px;\n"
                                       "color: white;\n"
                                       "}")
        self.progressBar.setProperty("value", 20)
        self.progressBar.setTextVisible(True)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(30, 10, 171, 21))
        self.title.setStyleSheet("border:none")
        self.title.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextEditable)
        self.title.setObjectName("title")
        self.video_format = QtWidgets.QLabel(self.widget)
        self.video_format.setGeometry(QtCore.QRect(210, 10, 41, 20))
        self.video_format.setStyleSheet("margin:none;\n"
                                        "background-color: #EAF2F6;\n"
                                        "border: 1px solid #EAF2F6;\n"
                                        "border - radius: 10;")
        self.video_format.setFrameShape(QtWidgets.QFrame.Box)
        self.video_format.setTextFormat(QtCore.Qt.PlainText)
        self.video_format.setAlignment(QtCore.Qt.AlignCenter)
        self.video_format.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.video_format.setObjectName("video_format")
        self.size = QtWidgets.QLabel(self.widget)
        self.size.setGeometry(QtCore.QRect(400, 10, 51, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.size.sizePolicy().hasHeightForWidth())
        self.size.setSizePolicy(sizePolicy)
        self.size.setStyleSheet("border:none;")
        self.size.setObjectName("size")
        self.delete_button = QtWidgets.QPushButton(self.widget)
        self.delete_button.setGeometry(QtCore.QRect(490, 10, 16, 16))
        self.delete_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_button.setStyleSheet("QPushButton {\n"
                                         "background-color: white;\n"
                                         "border: none\n"
                                         "}")
        self.delete_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/bin.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setIconSize(QtCore.QSize(12, 12))
        self.delete_button.setObjectName("delete_button")
        self.stop_button = QtWidgets.QPushButton(self.widget)
        self.stop_button.setGeometry(QtCore.QRect(470, 10, 16, 16))
        self.stop_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_button.setStyleSheet("QPushButton {\n"
                                       "background-color: white;\n"
                                       "border: none\n"
                                       "}")
        self.stop_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/stop.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(icon2)
        self.stop_button.setIconSize(QtCore.QSize(12, 12))
        self.stop_button.setObjectName("stop_button")
        self.Converter_404 = QtWidgets.QFrame(self.centralwidget)
        self.Converter_404.setGeometry(QtCore.QRect(180, 0, 661, 520))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Converter_404.sizePolicy().hasHeightForWidth())
        self.Converter_404.setSizePolicy(sizePolicy)
        self.Converter_404.setVisible(False)
        self.Converter_404.setStyleSheet("background-color: #ECF3FA; ")
        self.Converter_404.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Converter_404.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Converter_404.setObjectName("Converter_404")
        self.l_404 = QtWidgets.QLabel(self.Converter_404)
        self.l_404.setGeometry(QtCore.QRect(180, 0, 661, 520))
        self.l_404.setObjectName("l_404")
        self.l_404.setPixmap(QtGui.QPixmap('image_404.jpg'))
        self.l_404.setScaledContents(True)
        self.User_404 = QtWidgets.QFrame(self.centralwidget)
        self.User_404.setGeometry(QtCore.QRect(180, 0, 661, 520))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.User_404.sizePolicy().hasHeightForWidth())
        self.User_404.setSizePolicy(sizePolicy)
        self.User_404.setVisible(False)
        self.User_404.setStyleSheet("background-color: #ECF3FA; ")
        self.User_404.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.User_404.setFrameShadow(QtWidgets.QFrame.Raised)
        self.User_404.setObjectName("User_404")
        self.l_404 = QtWidgets.QLabel(self.User_404)
        self.l_404.setGeometry(QtCore.QRect(180, 0, 661, 520))
        self.l_404.setObjectName("l_404")
        self.l_404.setPixmap(QtGui.QPixmap('image_404.jpg'))
        self.l_404.setScaledContents(True)
        self.Side_bar = QtWidgets.QFrame(self.centralwidget)
        self.Side_bar.setGeometry(QtCore.QRect(0, 0, 181, 521))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Side_bar.sizePolicy().hasHeightForWidth())
        self.Side_bar.setSizePolicy(sizePolicy)
        self.Side_bar.setStyleSheet("align-items: left;\n"
                                    "border:none;")
        self.Side_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Side_bar.setObjectName("Side_bar")
        self.groupBox = QtWidgets.QGroupBox(self.Side_bar)
        self.groupBox.setGeometry(QtCore.QRect(0, 165, 181, 211))
        self.groupBox.setStyleSheet("align-items: left;\n"
                                    "display: flex;\n"
                                    "flex-wrap: wrap;\n"
                                    "border:none;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, -1, 1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Download_side_button = QtWidgets.QPushButton(self.groupBox)
        self.Download_side_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Download_side_button.sizePolicy().hasHeightForWidth())
        self.Download_side_button.setSizePolicy(sizePolicy)
        self.Download_side_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Download_side_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Download_side_button.setStyleSheet("QPushButton{\n"
                                                "box-sizing: border-box;\n"
                                                "padding-right: 40px;\n"
                                                "text-align: right;\n"
                                                "border: none}\n"
                                                "QPushButton:hover{\n"
                                                "background: #F7FAFD;\n"
                                                "border-left: 2px solid #034460}")
        icon = QtGui.QIcon.fromTheme("download_icon")
        icon.addPixmap(QtGui.QPixmap(":/images/download.png"),
                       QtGui.QIcon.Active, QtGui.QIcon.On)
        self.Download_side_button.setIcon(icon)
        self.Download_side_button.setIconSize(QtCore.QSize(14, 14))
        self.Download_side_button.setDefault(True)
        self.Download_side_button.clicked.connect(self.side_bottuns)
        self.Download_side_button.setObjectName("Download_side_button")
        self.verticalLayout.addWidget(self.Download_side_button)
        self.Converter_side_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Converter_side_button.sizePolicy().hasHeightForWidth())
        self.Converter_side_button.setSizePolicy(sizePolicy)
        self.Converter_side_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Converter_side_button.setStyleSheet("QPushButton{\n"
                                                 "box-sizing: border-box;\n"
                                                 "padding-right: 40px;\n"
                                                 "text-align: right;\n"
                                                 "border: none}\n"
                                                 "QPushButton:hover{\n"
                                                 "background: #F7FAFD;\n"
                                                 "border-left: 2px solid #034460}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/Converter.png"),
                        QtGui.QIcon.Active, QtGui.QIcon.On)
        self.Converter_side_button.setIcon(icon3)
        self.Converter_side_button.setIconSize(QtCore.QSize(14, 14))
        self.Converter_side_button.clicked.connect(self.side_bottuns)
        self.Converter_side_button.setObjectName("Converter_side_button")
        self.verticalLayout.addWidget(self.Converter_side_button)
        self.User_side_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.User_side_button.sizePolicy().hasHeightForWidth())
        self.User_side_button.setSizePolicy(sizePolicy)
        self.User_side_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.User_side_button.setStyleSheet("QPushButton{\n"
                                            "box-sizing: border-box;\n"
                                            "padding-right: 70px;\n"
                                            "text-align: right;\n"
                                            "border: none}\n"
                                            "QPushButton:hover{\n"
                                            "background: #F7FAFD;\n"
                                            "border-left: 2px solid #034460}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/User.png"),
                        QtGui.QIcon.Active, QtGui.QIcon.On)
        self.User_side_button.setIcon(icon4)
        self.User_side_button.setIconSize(QtCore.QSize(14, 14))
        self.User_side_button.clicked.connect(self.side_bottuns)
        self.User_side_button.setObjectName("User_side_button")
        self.verticalLayout.addWidget(self.User_side_button)
        self.Settingsr_side_button_2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Settingsr_side_button_2.sizePolicy().hasHeightForWidth())
        self.Settingsr_side_button_2.setSizePolicy(sizePolicy)
        self.Settingsr_side_button_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Settingsr_side_button_2.setStyleSheet("QPushButton{\n"
                                                   "box-sizing: border-box;\n"
                                                   "padding-right: 50px;\n"
                                                   "text-align: right;\n"
                                                   "border: none}\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "QPushButton:hover{\n"
                                                   "background: #F7FAFD;\n"
                                                   "\n"
                                                   "border-left: 2px solid #034460}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/Settings.png"),
                        QtGui.QIcon.Active, QtGui.QIcon.On)
        self.Settingsr_side_button_2.setIcon(icon5)
        self.Settingsr_side_button_2.setIconSize(QtCore.QSize(14, 14))
        self.Settingsr_side_button_2.setObjectName("Settingsr_side_button_2")
        self.verticalLayout.addWidget(self.Settingsr_side_button_2)
        self.main_icon = QtWidgets.QLabel(self.Side_bar)
        self.main_icon.setGeometry(QtCore.QRect(40, 20, 101, 41))
        self.main_icon.setText("")
        self.main_icon.setPixmap(QtGui.QPixmap(":/images/Everything.png"))
        self.main_icon.setObjectName("main_icon")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        Abyss.setCentralWidget(self.centralwidget)

        self.retranslateUi(Abyss)
        QtCore.QMetaObject.connectSlotsByName(Abyss)

    def retranslateUi(self, Abyss):
        _translate = QtCore.QCoreApplication.translate
        Abyss.setWindowTitle(_translate("Abyss", "MainWindow"))
        self.Body_header.setText(_translate("Abyss", "Downloader"))
        self.header2.setText(_translate("Abyss", "Downloads"))
        self.download_button.setText(_translate("Abyss", "Download"))
        self.input_text.setPlaceholderText(
            _translate("Abyss", "Paste url here"))
        self.title.setText(_translate("Abyss", "run town for the win .mp4"))
        self.video_format.setText(_translate("Abyss", "Mp4"))
        self.size.setText(_translate("Abyss", "20mb/2gb"))
        self.Download_side_button.setText(
            _translate("Abyss", "      Download"))
        self.Converter_side_button.setText(
            _translate("Abyss", "      Converter"))
        self.User_side_button.setText(_translate("Abyss", "      User"))
        self.Settingsr_side_button_2.setText(
            _translate("Abyss", "      Settings"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Abyss = QtWidgets.QMainWindow()
    ui = Ui_Abyss()
    ui.setupUi(Abyss)
    Abyss.show()
    sys.exit(app.exec_())
