
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 431)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(15, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(60, 10, 461, 23))
        self.url_input.setObjectName("url_input")
        self.location_label = QtWidgets.QLabel(self.centralwidget)
        self.location_label.setGeometry(QtCore.QRect(15, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.location_label.setFont(font)
        self.location_label.setObjectName("location_label")
        self.location_input = QtWidgets.QLineEdit(self.centralwidget)
        self.location_input.setGeometry(QtCore.QRect(110, 50, 311, 23))
        self.location_input.setObjectName("location_input")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(430, 50, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.browse.setFont(font)
        self.browse.setObjectName("browse")
        self.quality_label = QtWidgets.QLabel(self.centralwidget)
        self.quality_label.setGeometry(QtCore.QRect(40, 85, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quality_label.setFont(font)
        self.quality_label.setObjectName("quality_label")
        self.quality_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.quality_comboBox.setGeometry(QtCore.QRect(110, 90, 81, 21))
        self.quality_comboBox.setObjectName("quality_comboBox")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.quality_comboBox.addItem("")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 130, 511, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.current_video = QtWidgets.QLabel(self.centralwidget)
        self.current_video.setGeometry(QtCore.QRect(210, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.current_video.setFont(font)
        self.current_video.setObjectName("current_video")
        self.total_video = QtWidgets.QLabel(self.centralwidget)
        self.total_video.setGeometry(QtCore.QRect(360, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total_video.setFont(font)
        self.total_video.setScaledContents(False)
        self.total_video.setObjectName("total_video")
        self.fetch_urls = QtWidgets.QPushButton(self.centralwidget)
        self.fetch_urls.setGeometry(QtCore.QRect(70, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fetch_urls.setFont(font)
        self.fetch_urls.setObjectName("fetch_urls")
        self.start_download = QtWidgets.QPushButton(self.centralwidget)
        self.start_download.setGeometry(QtCore.QRect(210, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start_download.setFont(font)
        self.start_download.setAutoFillBackground(False)
        self.start_download.setStyleSheet("")
        self.start_download.setObjectName("start_download")
        self.stop_downloading = QtWidgets.QPushButton(self.centralwidget)
        self.stop_downloading.setGeometry(QtCore.QRect(350, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stop_downloading.setFont(font)
        self.stop_downloading.setObjectName("stop_downloading")
        self.status_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.status_box.setGeometry(QtCore.QRect(30, 220, 481, 161))
        self.status_box.setObjectName("status_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Multi-Downloader"))
        self.url_label.setText(_translate("MainWindow", "URL :"))
        self.url_input.setToolTip(_translate("MainWindow", "<html><head/><body><p>Place the video playlist url here</p></body></html>"))
        self.location_label.setText(_translate("MainWindow", "Save Location : "))
        self.browse.setToolTip(_translate("MainWindow", "<html><head/><body><p>Choose where do you want to save the playlist</p></body></html>"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.quality_label.setText(_translate("MainWindow", "Quality : "))
        self.quality_comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pick the quality you want</p></body></html>"))
        self.quality_comboBox.setItemText(0, _translate("MainWindow", "1080p"))
        self.quality_comboBox.setItemText(1, _translate("MainWindow", "720p"))
        self.quality_comboBox.setItemText(2, _translate("MainWindow", "480p"))
        self.quality_comboBox.setItemText(3, _translate("MainWindow", "360p"))
        self.quality_comboBox.setItemText(4, _translate("MainWindow", "240p"))
        self.quality_comboBox.setItemText(5, _translate("MainWindow", "144p"))
        self.progressBar.setToolTip(_translate("MainWindow", "<html><head/><body><p>the Prograss of downloading the videos</p></body></html>"))
        self.current_video.setText(_translate("MainWindow", "Current Video : "))
        self.total_video.setText(_translate("MainWindow", "  Total Videos : "))
        self.fetch_urls.setToolTip(_translate("MainWindow", "<html><head/><body><p>get the urls from the playlist</p></body></html>"))
        self.fetch_urls.setText(_translate("MainWindow", "Fetch URLs"))
        self.start_download.setToolTip(_translate("MainWindow", "<html><head/><body><p>start downloading the playlist of the videos</p></body></html>"))
        self.start_download.setText(_translate("MainWindow", "Start Downlaod"))
        self.stop_downloading.setToolTip(_translate("MainWindow", "<html><head/><body><p>Stop the process of downloading</p></body></html>"))
        self.stop_downloading.setText(_translate("MainWindow", "Stop Downloading"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())