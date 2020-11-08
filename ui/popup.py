from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from main import * 
import ui.popup_r
from engine.downloads import VideoDownloader



class Ui_Add(object):

        def __init__(self, url):
                self.url = url
                vid = VideoDownloader(self.url)
                self.set_title = vid.video_title()
                self.set_lenght = vid.video_time()
                self.set_size = vid.formated_size()
                self.thumbnail = vid.image_display()

        def StartDownload(self):
                self.download_clicker
       
        def setupUi(self, Add):
                Add.setObjectName("Add")
                Add.resize(394, 198)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/popup/widow_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                Add.setWindowIcon(icon)
                Add.setStyleSheet("background-color: white\n")
                Add.setModal(False)
                self.Thumbnail = QtWidgets.QLabel(Add)
                self.Thumbnail.setGeometry(QtCore.QRect(30, 30, 131, 121))
                self.Thumbnail.setStyleSheet("border-radius: 4px;\n"
        "")
                self.Thumbnail.setObjectName("Thumbnail")
                self.Thumbnail.setPixmap(QtGui.QPixmap(self.thumbnail))
                self.Thumbnail.setScaledContents(True)
                self.title = QtWidgets.QLabel(Add)
                self.title.setGeometry(QtCore.QRect(180, 30, 231, 31))
                self.title.setStyleSheet("align-text: none;\n"
        "overflow: hidden;\n"
        "text-overflow: ellipsis;\n"
        "")
                self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.title.setObjectName("title")
                self.lenght = QtWidgets.QLabel(Add)
                self.lenght.setGeometry(QtCore.QRect(180, 60, 61, 21))
                self.lenght.setStyleSheet("color:#828282")
                self.lenght.setObjectName("lenght")
                self.size = QtWidgets.QLabel(Add)
                self.size.setGeometry(QtCore.QRect(180, 82, 61, 21))
                self.size.setStyleSheet("color:#828282")
                self.size.setObjectName("size")
                self.Download_botton_container = QtWidgets.QWidget(Add)
                self.Download_botton_container.setGeometry(QtCore.QRect(170, 130, 161, 21))
                self.Download_botton_container.setStyleSheet("display: flex;\n"
        "border: 1px  #034460;\n"
        "box-sizing: border-box;\n"
        "font-family: jos;\n"
        "font-size: 10px;")
                self.Download_botton_container.setObjectName("Download_botton_container")
                self.download_button = QtWidgets.QPushButton(self.Download_botton_container)
                self.download_button.setGeometry(QtCore.QRect(10, 0, 75, 22))
                self.download_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.download_button.setStyleSheet("border: 2px solid #034460;\n"
        "background-color:  #034460;\n"
        "color: white")
                self.download_button.setObjectName("download_button")
                self.video_format_select = QtWidgets.QComboBox(self.Download_botton_container)
                self.video_format_select.addItems(['360p', '480p','720p', '1080p' ])
                self.video_format_select.setGeometry(QtCore.QRect(78, 0, 81, 22))
                self.video_format_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.video_format_select.setStyleSheet("QComboBox{border: none;\n"
"combobox-popup: 0;\n"
"border: 1px solid #034460;\n"
"}\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"overflow : none;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: 1px  #034460;\n"
"color:#034460;\n"
"   }\n"
"QComboBox::down-arrow {\n"
"    image: url(\":/popup/Stroke 169.png\");\n"
"}")
                self.video_format_select.setObjectName("video_format_select")

                self.retranslateUi(Add)
                QtCore.QMetaObject.connectSlotsByName(Add)

        def retranslateUi(self, Add):
                _translate = QtCore.QCoreApplication.translate
                self.title.setText(_translate("Add", f"{self.set_title}.mp4"))
                self.lenght.setText(_translate("Add", self.set_lenght))
                self.size.setText(_translate("Add", self.set_size))
                self.download_button.setText(_translate("Add", "Download"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add = QtWidgets.QDialog()
    ui = Ui_Add()
    ui.setupUi(Add)
    Add.show()
    sys.exit(app.exec_())
